# Snowfall

## Overview
Snowfall represents the accumulated solid precipitation (snow, ice pellets, snow grains) reaching the Earth's surface over a specified period, expressed as liquid water equivalent. This critical variable is essential for water resource management, winter weather analysis, and understanding the cryospheric component of the climate system.

## Scientific Description
In ERA5, snowfall is defined as the water equivalent depth of solid precipitation reaching the surface. The variable represents:

- **Snow**: Ice crystals formed by deposition and aggregation in clouds
- **Ice pellets**: Frozen raindrops
- **Snow grains**: Very small white opaque ice particles
- **Graupel**: Soft hail formed by riming

The snowfall rate is determined by:
1. **Cloud microphysics**: Ice crystal formation and growth processes
2. **Temperature profile**: Determines whether precipitation falls as rain or snow
3. **Humidity**: Affects sublimation during descent
4. **Precipitation intensity**: Total condensation rate in clouds

### Rain-Snow Partitioning
The phase of precipitation depends primarily on temperature:
- **All snow**: Near-surface temperature < ~0°C (varies with humidity)
- **Mixed**: Temperature ~0-2°C
- **All rain**: Temperature > ~2°C

More sophisticated schemes consider:
- Wet-bulb temperature (accounts for evaporative cooling)
- Humidity effects on melting level
- Precipitation intensity (heavy snow can fall through warmer air)

The snowfall value is in liquid water equivalent, not snow depth. Fresh snow density varies:
- **Dry snow**: 50-100 kg m⁻³ (10-20:1 snow-to-liquid ratio)
- **Average**: 100-150 kg m⁻³ (7-10:1 ratio)
- **Wet snow**: 150-300 kg m⁻³ (3-7:1 ratio)

## Units
- **Standard Unit**: Metres (m) of liquid water equivalent
- **Common Alternative**: Millimetres (mm) of water equivalent - multiply by 1000
- **Alternative Units**: kg m⁻² (numerically equivalent to mm water equivalent)
- **Snow Depth**: Multiply by typical snow-to-liquid ratio (5-15) to estimate depth
- **Typical Range**: 
  - Trace to 50 mm water equivalent per day in most snowfall events
  - Extreme blizzards: >100 mm water equivalent (>1 meter of snow depth)

## Applications in Climate Research

### Water Resources and Hydrology
Snowfall is critical for water management:
- **Snowpack accumulation**: Winter snow storage for spring/summer melt
- **Streamflow forecasting**: Snowmelt dominates runoff in many regions
- **Reservoir management**: Snow water equivalent predicts water availability
- **Drought monitoring**: Below-normal snowfall reduces water supply

### Climate Change Indicators
Snowfall changes reflect warming climate:
- **Rain-snow transition elevation**: Rising with temperature increase
- **Seasonal snow cover duration**: Decreasing in most regions
- **Spring snow disappearance**: Occurring earlier
- **Glacier mass balance**: Accumulation vs. ablation

### Winter Weather and Hazards
Snowfall affects human activities:
- **Transportation disruption**: Road closures, airport delays
- **Infrastructure loading**: Building roofs, power lines
- **Economic impacts**: Snow removal costs, business interruption
- **Winter recreation**: Skiing, snowmobiling depend on snowfall

### Ecosystems and Agriculture
Snow cover impacts:
- **Insulation**: Protects plants, soil organisms from extreme cold
- **Spring soil moisture**: Snowmelt recharges soil water
- **Phenology**: Snowmelt timing affects plant growing season
- **Wildlife**: Migration patterns, food availability

### Cryosphere Studies
Snowfall contributes to:
- **Glacier accumulation**: Positive mass balance component
- **Sea ice formation**: Snow-ice conversion on thin ice
- **Permafrost insulation**: Snow depth affects ground temperatures
- **Ice sheet mass balance**: Accumulation zones of Greenland, Antarctica

## Related Variables
- **total_precipitation**: Snowfall + rainfall
- **2m_temperature**: Determines rain vs. snow
- **surface_temperature**: Ground temperature affects snow accumulation
- **10m_wind_speed**: Wind redistributes snow (blowing snow, drifts)
- **surface_net_solar_radiation**: Affects snowmelt and sublimation

## Mathematical Relationships
- **Total Precipitation**: Ptotal = Snowfall + Rainfall (liquid equivalent)
- **Snow Depth Estimation**: Depth ≈ Snowfall × ρwater / ρsnow where ρ is density
- **Typical Conversion**: 10 mm water equivalent ≈ 100 mm (10 cm) fresh snow depth
- **Snowmelt Energy**: Qmelt = ρice × Lf × Snowfall where Lf is latent heat of fusion (~334 kJ kg⁻¹)

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily accumulations from hourly data
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Physical Process**: Model microphysics and phase determination
- **Units**: Liquid water equivalent (not snow depth)
- **Availability**: 1940 to present

## Quality Considerations
- **Phase determination**: Threshold temperature for rain-snow transition has uncertainty
- **Undercatch**: Solid precipitation observations suffer from gauge undercatch (wind effects)
- **Density assumption**: Water equivalent to depth conversion requires density estimate
- **Blowing snow**: Wind redistribution not captured at model scale
- **Sublimation**: Some snow sublimates during descent (accounted in model)
- **Mixed precipitation**: Freezing rain, sleet classification challenges
- **Mountain regions**: Orographic enhancement and terrain effects

## Physical Context

### Snow Crystal Formation
Snowflakes form through:
1. **Nucleation**: Ice crystals form on ice nuclei in supercooled clouds
2. **Deposition**: Water vapor deposits directly onto ice crystals
3. **Aggregation**: Crystals collide and stick together
4. **Riming**: Supercooled droplets freeze onto crystals (graupel formation)

Crystal type depends on temperature and supersaturation:
- Plates, dendrites, needles, columns (various T, humidity conditions)

### Snowfall Processes
- **Stratiform snow**: From nimbostratus; steady, light-moderate intensity
- **Convective snow**: From cumulonimbus; heavy, brief snow showers
- **Orographic snow**: Enhanced by terrain lifting; very heavy in mountains
- **Lake-effect snow**: Cold air over warm water; intense localized bands

### Geographic Patterns
- **Polar regions**: Year-round snowfall potential
- **Mid-latitudes**: Seasonal (winter) snowfall
- **Subtropics**: Rare, high-elevation only
- **Tropics**: High mountains only (>4000-5000 m elevation)

## Practical Interpretation
- **Snowfall < 5 mm water**: Light snow (< 5 cm depth); minor impacts
- **Snowfall 5-15 mm water**: Moderate snow (5-15 cm depth); travel impacts
- **Snowfall 15-30 mm water**: Heavy snow (15-30 cm depth); significant disruption
- **Snowfall > 30 mm water**: Extreme snow (> 30 cm depth); major impacts, blizzard potential

### Seasonal Patterns
- **Early winter**: Lake-effect dominant near large water bodies
- **Mid-winter**: Synoptic storms, coldest temperatures
- **Late winter**: Heavier, wetter snow (marginal temperatures)
- **Spring**: Rapidly decreasing snowfall, mix with rain more common

## Snow Water Equivalent (SWE)
Snowfall accumulates as snowpack with total SWE = ∫ Snowfall dt - Melt - Sublimation

Peak SWE occurs typically:
- **Maritime climates**: Mid-winter (warm, melt occurs all winter)
- **Continental climates**: Late winter/early spring (cold, accumulation continues)

## Climate Change Impacts
Observed and projected snowfall changes:
1. **Total snowfall**: Generally decreasing in most regions (except coldest areas)
2. **Rain-on-snow events**: Increasing (warmer temperatures)
3. **Snowfall intensity**: May increase in cold regions (more moisture available)
4. **Elevation shift**: Snow zone moving upward in mountains (~150 m per °C)
5. **Seasonal shift**: Earlier end to snow season, later start

## Mountain Snow
Elevation effects dominate:
- **Precipitation gradient**: Often increases with elevation (orographic enhancement)
- **Phase gradient**: Rain at low elevation, snow at high elevation
- **Aspect effects**: Windward slopes receive more snow than lee slopes
- **Temperature lapse**: ~6-7°C per km decrease in temperature

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Pruppacher, H. R., & Klett, J. D. (1997). *Microphysics of Clouds and Precipitation* (2nd ed.). Springer.
3. Sturm, M., et al. (2010). Estimating snow water equivalent using snow depth data and climate classes. *Journal of Hydrometeorology*, 11(6), 1380-1394.
4. Barnett, T. P., et al. (2005). Potential impacts of a warming climate on water availability in snow-dominated regions. *Nature*, 438(7066), 303-309.
