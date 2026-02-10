# Sea Ice Thickness

## Overview
Sea ice thickness represents the vertical extent of sea ice, measuring the distance from the ice surface to the ice-ocean interface. Combined with ice area fraction (concentration), thickness determines ice volume, which is the primary measure of the total sea ice mass in the climate system.

## Scientific Description
Sea ice thickness varies dramatically across space and time:

**Range**: From centimeters (new ice) to several meters (multi-year Arctic ice, pressure ridges >10 m)

In ERA5, sea ice thickness is computed by the ocean-ice model component (NEMO-LIM) and represents:
- **Level ice**: Undeformed ice thickness
- **Grid-cell mean**: Average thickness over ice-covered portion
- **Effective thickness**: Actual thickness where ice exists (not area-averaged over entire grid cell)

The thickness evolves through:

1. **Thermodynamic growth/melt**:
   - Bottom freezing: Ocean heat loss → ice growth
   - Top melt: Solar radiation → ice ablation
   - Bottom melt: Ocean heat → basal melting
   - Lateral melt: Leads absorption of solar radiation

2. **Dynamic processes**:
   - Ridging: Ice deformation creating thick ice
   - Rafting: Ice sheets overriding each other
   - Convergence: Ice compression
   - Divergence: Ice spreading (doesn't change thickness, but creates leads)

## Units
- **Standard Unit**: Metres (m)
- **Typical Values**:
  - New ice: 0.0-0.1 m
  - Young ice: 0.1-0.3 m
  - First-year ice: 0.3-2.0 m
  - Multi-year Arctic ice: 2.0-4.0 m (declining to 1.5-3.0 m in recent years)
  - Pressure ridges: 5-15 m
  - Antarctic ice: 0.5-1.5 m (mostly seasonal)

## Applications in Climate Research

### Ice Volume and Mass Balance
Thickness combined with area gives total ice volume:
- **Volume = ∫ (thickness × area) over domain**
- **Mass balance**: Volume tendency = Growth - Melt - Export
- **Climate indicator**: Volume integrates both area and thickness changes
- **Long-term trends**: Volume declining faster than area in Arctic

### Climate Change Assessment
Ice thickness is sensitive climate indicator:
- **Thermodynamic thinning**: Warmer atmosphere/ocean → thinner ice
- **Multi-year ice decline**: Thick old ice being replaced by thin annual ice
- **Ice age**: Thinner ice survives shorter, creating feedback
- **Projections**: Models predict continued thinning

### Ocean-Atmosphere Heat Exchange
Thickness controls heat flux through ice:
- **Thin ice (<0.5 m)**: Substantial heat leakage to atmosphere
- **Thick ice (>2 m)**: Good insulation, minimal heat flux
- **Winter heat loss**: Thin ice areas critical for ocean ventilation
- **Polynya formation**: Thin ice more prone to opening

### Mechanical Strength and Navigation
Thickness determines ice mechanical properties:
- **Ice strength**: Increases with thickness
- **Ship navigation**: Icebreaker capability depends on thickness
- **Offshore operations**: Ice loads on structures
- **Ice roads**: Safe thickness for travel (typically >0.5 m)

### Ecosystem Implications
Ice thickness affects marine ecosystems:
- **Light penetration**: Thin ice allows more light for under-ice algae
- **Snow cover**: Thick ice supports more snow, reducing light
- **Habitat**: Thick ridges provide seal dens, polar bear habitat
- **Melt ponds**: Form preferentially on thick multi-year ice

### Model Validation and Improvement
Ice thickness tests model physics:
- **Process representation**: Thermodynamics, dynamics
- **Ocean-ice coupling**: Heat and momentum exchange
- **Climate sensitivity**: Thickness response to forcing

## Related Variables
- **sea_ice_area_fraction**: Ice extent; volume = thickness × area
- **snow_depth_on_sea_ice**: Snow insulates ice, affects growth/melt
- **sea_surface_temperature**: SST constrained near freezing under ice
- **2m_temperature**: Air temperature drives surface energy balance
- **10m_u/v_component_of_wind**: Wind stress drives ice motion and deformation

## Mathematical Relationships
- **Ice Volume per Unit Area**: h = V/A where h is thickness, V is volume
- **Thermodynamic growth rate**: dh/dt = (Q_top + Q_bottom) / (ρ_ice × L_f)
  - Q = heat flux, ρ_ice = ice density (~920 kg m⁻³), L_f = latent heat of fusion
- **Ridging**: Thicker ice produced from thinner ice through deformation
- **Conductive heat flux through ice**: Q = k × (T_bottom - T_top) / h
  - k = thermal conductivity (~2 W m⁻¹ K⁻¹)

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily values (state variable, not accumulation)
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Model Component**: NEMO-LIM ocean-ice model
- **Availability**: 1940 to present
- **Quality**: Constrained by limited thickness observations, especially pre-satellite era

## Quality Considerations
- **Observational scarcity**: Thickness observations sparse compared to concentration
- **Satellite altimetry**: ICESat, CryoSat-2 provide thickness data (post-2003)
- **Submarine data**: Historical military submarines, limited coverage
- **Model dependence**: Thickness more model-dependent than concentration
- **Ridging representation**: Sub-grid scale ridges parameterized
- **Pre-satellite era**: Thickness estimates highly uncertain before ~2000

## Physical Context

### Ice Growth (Winter)
Thickness increases when ocean loses heat:

**Stefan's Law** (approximate):
h² = (2k/ρL_f) × ∫ FDD

where FDD = freezing degree-days (cumulative T < 0°C)

Growth rate decreases with thickness (insulation effect):
- Thin ice: 1-5 cm/day
- 1 m ice: 0.5-1 cm/day  
- 2 m ice: 0.1-0.5 cm/day

### Ice Melt (Summer)
Thickness decreases from:
- **Top melt**: 0.5-2 m per summer in Arctic
- **Bottom melt**: 0.5-1 m per summer
- **Lateral melt**: Important for small floes

Melt rate depends on:
- Solar radiation (June-July maximum)
- Air temperature
- Ocean heat content
- Melt pond coverage (reduces albedo)

### Pressure Ridges
Convergent ice motion creates thick ice:
- **Ridge height**: 1-5 m above surface
- **Keel depth**: 5-40 m below surface (conservation of volume)
- **Sail-to-keel ratio**: Typically 1:4 to 1:6
- **Strength**: Provides mechanical strength to ice pack

## Regional Characteristics

**Arctic**:
- **Central Arctic**: Historically 3-4 m multi-year ice, now 2-3 m
- **Beaufort/Chukchi**: Thick ice from convergence
- **East Siberian**: Younger, thinner ice
- **Fram Strait**: Ice export region

**Antarctic**:
- **Weddell Sea**: Thickest Antarctic ice (1-2 m)
- **Ross Sea**: Seasonal ice (0.5-1.5 m)
- **Amundsen/Bellingshausen**: Thin seasonal ice

## Practical Interpretation
- **h < 0.1 m**: New/young ice, fragile
- **h = 0.1-0.3 m**: Young ice, navigable by icebreakers
- **h = 0.3-0.7 m**: First-year thin ice
- **h = 0.7-1.2 m**: First-year medium ice
- **h = 1.2-2.0 m**: First-year thick ice
- **h > 2.0 m**: Multi-year ice (primarily Arctic)
- **h > 5 m**: Pressure ridges

## Observed Trends
**Arctic** (satellite era, 1979-present):
- Average thickness decline: ~1.7 m to ~1.3 m (central Arctic)
- Multi-year ice fraction: Declining from ~50% to ~20% of total
- Younger ice: Mean age decreased from ~6 years to ~3 years
- Seasonal range: Amplitude increasing (thinner in summer)

**Antarctic**:
- Regional variability: Some areas thickening, others thinning
- Less clear long-term trend than Arctic
- Predominantly seasonal ice (1 year or less)

## Ice-Ocean-Atmosphere Coupling
Thickness influences multiple feedbacks:

1. **Ice-Albedo Feedback**: Thin ice → more melt → less ice
2. **Ice-Growth Feedback**: Thin ice → faster growth → partially compensating
3. **Snow-Ice Feedback**: Thin ice supports less snow, affects albedo
4. **Heat Flux Feedback**: Thin ice → more heat loss → ocean cooling

## Climate Change Implications
Projected changes:
- **Continued thinning**: All scenarios show declining thickness
- **Loss of multi-year ice**: Transition to seasonal ice regime
- **Ice-free summers**: Requires thickness approaching zero
- **Increased variability**: Thinner ice more susceptible to variability

## Satellite Measurements
Key missions for thickness observation:
- **ICESat (2003-2009)**: Laser altimetry
- **CryoSat-2 (2010-present)**: Radar altimetry
- **ICESat-2 (2018-present)**: Laser altimetry
- **Method**: Measure ice freeboard, convert to thickness using assumptions

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Kwok, R., & Rothrock, D. A. (2009). Decline in Arctic sea ice thickness from submarine and ICESat records: 1958–2008. *Geophysical Research Letters*, 36(15), L15501.
3. Stroeve, J., & Notz, D. (2018). Changing state of Arctic sea ice across all seasons. *Environmental Research Letters*, 13(10), 103001.
4. Schweiger, A., et al. (2011). Uncertainty in modeled Arctic sea ice volume. *Journal of Geophysical Research: Oceans*, 116(C8), C00D06.
