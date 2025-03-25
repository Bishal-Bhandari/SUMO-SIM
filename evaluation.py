import json
import pandas as pd
from scipy.stats import ttest_rel
import numpy as np


def load_json(file_path):
    """Load JSON data into a DataFrame."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return pd.DataFrame([agent['PersonInfo'] | agent['Walk'] | agent['Ride'] for agent in data])


def calculate_metrics(df):
    """Calculate agent-centric metrics."""
    df['TotalTravelTime'] = df['duration']
    df['WalkingDuration'] = df['Walk1'].apply(lambda x: x['duration']) + df['Walk2'].apply(lambda x: x['duration'])
    df['WalkingDistance'] = df['Walk1'].apply(lambda x: x['routeLength']) + df['Walk2'].apply(
        lambda x: x['routeLength'])
    df['TimeLoss'] = df['Walk1'].apply(lambda x: x['timeLoss']) + df['Walk2'].apply(lambda x: x['timeLoss']) + df[
        'timeLoss']
    df['RideEfficiency'] = (df['Ride'].apply(lambda x: x['duration']) / df['TotalTravelTime']) * 100
    return df


def compare_efficiency(gt_df, pred_df):
    """Compare ground truth vs. predicted metrics."""
    metrics = ['TotalTravelTime', 'WalkingDuration', 'WalkingDistance', 'TimeLoss', 'RideEfficiency', 'waitingTime']
    comparison = {}

    for metric in metrics:
        gt_mean = gt_df[metric].mean()
        pred_mean = pred_df[metric].mean()
        improvement = (gt_mean - pred_mean) / gt_mean * 100 if gt_mean != 0 else 0
        t_stat, p_value = ttest_rel(gt_df[metric], pred_df[metric])

        comparison[metric] = {
            'GroundTruth_Mean': gt_mean,
            'Predicted_Mean': pred_mean,
            'Improvement (%)': improvement,
            'p-value': p_value
        }

    return pd.DataFrame(comparison).T


def calculate_system_metrics(gt_df, pred_df):
    """Calculate system-centric metrics."""

    def _system_metrics(df):
        total_distance = df['Ride'].apply(lambda x: x['routeLength']).sum()
        total_time = df['TotalTravelTime'].sum()
        return {
            'AvgSpeed (m/s)': total_distance / total_time,
            'AvgTimeLoss': df['TimeLoss'].mean()
        }

    return {
        'GroundTruth': _system_metrics(gt_df),
        'Predicted': _system_metrics(pred_df)
    }


# Load data
gt_df = load_json('personinfo.json')
pred_df = load_json('personinfo_gen_stop.json')

# Calculate agent metrics
gt_metrics = calculate_metrics(gt_df)
pred_metrics = calculate_metrics(pred_df)

# Compare efficiency
efficiency_comparison = compare_efficiency(gt_metrics, pred_metrics)
print("Agent-Centric Efficiency Comparison:\n")
print(efficiency_comparison.to_markdown())

# System metrics
system_comparison = calculate_system_metrics(gt_metrics, pred_metrics)
print("\nSystem-Centric Efficiency Comparison:\n")
print(pd.DataFrame(system_comparison).to_markdown())

# Check for identical datasets
if gt_metrics.equals(pred_metrics):
    print("\n⚠️ Warning: Ground truth and predicted datasets are identical!")