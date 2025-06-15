# Interactive sunburst plot (requires plotly)
import plotly.express as px

risk_by_vehicle = df.groupby(['Make', 'Model']).agg(
    ClaimRate=('HasClaim', 'mean'),
    AvgSeverity=('ClaimSeverity', 'mean')
).reset_index()

fig = px.sunburst(
    risk_by_vehicle,
    path=['Make', 'Model'],
    values='ClaimRate',
    color='AvgSeverity',
    color_continuous_scale='Reds'
)
fig.update_layout(title="Vehicle Risk Hierarchy")
fig.show()