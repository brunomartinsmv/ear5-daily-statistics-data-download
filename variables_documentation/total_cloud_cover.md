# Total Cloud Cover

## Overview
Total cloud cover represents the fraction of the sky covered by clouds at all levels, expressed as a value between 0 (clear sky) and 1 (completely overcast). This variable integrates cloud presence throughout the entire atmospheric column and is fundamental for understanding radiation balance, precipitation processes, and weather patterns.

## Scientific Description
Total cloud cover in ERA5 represents the fraction of a grid cell covered by clouds when viewed from above, considering cloud overlap from all atmospheric levels. The variable accounts for:

- **Low clouds**: Below ~2 km (stratus, stratocumulus, cumulus)
- **Middle clouds**: 2-6 km (altocumulus, altostratus)  
- **High clouds**: Above 6 km (cirrus, cirrostratus, cirrocumulus)

Cloud overlap assumptions affect total cloud cover:
- **Random overlap**: Assumes clouds at different levels independently positioned
- **Maximum overlap**: Assumes clouds in adjacent layers overlap maximally
- **Mixed schemes**: Combination approaches used in ERA5

Total cloud cover ≤ Sum of individual layer cloud covers (due to overlap)

## Units
- **Standard Unit**: Fraction (0-1)
- **Alternative**: Percent (0-100%) - multiply by 100
- **Typical Values**:
  - Clear sky: 0.0-0.1
  - Partly cloudy: 0.1-0.5
  - Mostly cloudy: 0.5-0.9
  - Overcast: 0.9-1.0

## Applications
- Radiation balance (clouds reduce solar, trap longwave)
- Weather forecasting and nowcasting
- Aviation (visibility, icing conditions)
- Solar energy (PV production strongly affected)
- Climate change (cloud feedbacks highly uncertain)
- Satellite remote sensing validation

## Related Variables
- low_cloud_cover, medium_cloud_cover, high_cloud_cover
- surface_net_solar_radiation
- surface_net_thermal_radiation  
- total_precipitation

## Data Characteristics
- Daily statistics from hourly values
- Spatial resolution: ~0.25° × 0.25°
- Model-derived with satellite constraints
- Availability: 1940 to present

## References
1. Hersbach, H., et al. (2020). *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Stubenrauch, C. J., et al. (2013). Assessment of global cloud datasets. *Bulletin of the American Meteorological Society*, 94(7), 1031-1049.
