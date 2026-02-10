# Surface Net Thermal Radiation

## Overview
Surface net thermal radiation (also called net longwave radiation) represents the net radiative flux in the thermal infrared (longwave) spectrum at the Earth's surface. It is the difference between upward emission from the surface and downward emission from the atmosphere, representing a continuous energy loss from the surface.

## Scientific Description
Net thermal radiation is defined as:

**Rn_thermal = LW↓ - LW↑**

where:
- LW↓ = downward longwave radiation from atmosphere
- LW↑ = upward longwave radiation from surface

Key characteristics:
- **Sign**: Typically negative (more upward than downward, net energy loss)
- **24-hour flux**: Operates day and night (unlike solar)
- **Greenhouse effect**: Downward component from atmospheric gases (H₂O, CO₂, etc.)

Surface emission (Stefan-Boltzmann):
**LW↑ = ε σ Ts⁴**
- ε = surface emissivity (~0.95-0.99 for natural surfaces)
- σ = Stefan-Boltzmann constant (5.67×10⁻⁸ W m⁻² K⁻⁴)
- Ts = surface temperature

Atmospheric emission depends on:
- Temperature profile
- Water vapor content (major greenhouse gas)
- Cloud cover (clouds emit as blackbodies)
- Other greenhouse gases

## Units
- Joules per square metre (J m⁻²) for accumulations
- Watts per square metre (W m⁻²) for instantaneous flux
- Typical daily mean: -60 to -100 W m⁻² (negative = net loss)

## Applications
- **Surface energy balance**: Cooling term at night
- **Nocturnal temperature**: Radiative cooling determines minimum temperature
- **Frost prediction**: Clear nights have large net longwave loss → frost
- **Greenhouse effect**: Downward component quantifies atmospheric warming
- **Climate change**: Changes in net thermal radiation with warming
- **Urban heat island**: Urban surfaces retain more heat due to longwave trapping

## Related Variables
- surface_net_solar_radiation: Together give total net radiation
- 2m_temperature: Affects upward emission
- total_cloud_cover: Clouds enhance downward radiation
- 2m_dewpoint_temperature: Water vapor affects downward radiation

## Physical Context
Clear sky vs. cloudy:
- **Clear sky**: Large net loss (50-100 W m⁻²), cold nights
- **Cloudy**: Smaller net loss (20-40 W m⁻²), warmer nights

Seasonal/diurnal patterns:
- **Desert**: Large diurnal range (clear skies, dry air)
- **Humid tropics**: Small range (moist atmosphere, clouds)
- **Winter**: Larger net loss (cold atmosphere emits less)

## References
1. Hersbach, H., et al. (2020). *Q. J. R. Meteorol. Soc.*, 146(730), 1999-2049.
2. Prata, A. J. (1996). A new long-wave formula for estimating downward clear-sky radiation. *Q. J. R. Meteorol. Soc.*, 122(533), 1127-1151.
