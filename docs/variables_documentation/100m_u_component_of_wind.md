# 100-Metre U Component of Wind

## Overview
The 100-metre U component of wind represents the zonal (east-west) wind component at 100 metres above the Earth's surface. This variable is particularly important for wind energy applications, as 100 metres approximates the hub height of modern utility-scale wind turbines.

## Scientific Description
The 100-metre U wind component follows the same meteorological convention as the 10-metre U component:
- **U > 0**: Eastward wind (wind from the west)
- **U < 0**: Westward wind (wind from the east)
- **U = 0**: No zonal flow

In ERA5, the 100-metre wind is diagnosed from the atmospheric model's vertical wind profile using similarity theory extended above the surface layer. The extrapolation accounts for:
- Surface roughness effects (diminishing with height)
- Atmospheric stability profile
- Vertical wind shear characteristics
- Transition toward free-atmosphere conditions

The 100-metre level typically lies:
- Above the roughness sublayer (immediate surface effects)
- Within or near the top of the surface layer (0-100 m)
- Below the Ekman layer (100-1000 m)
- In a transition zone between surface-influenced and free-atmosphere flow

Wind speed generally increases with height due to reduced surface friction, making the 100-metre wind stronger than the 10-metre wind.

## Units
- **Standard Unit**: Metres per second (m s⁻¹)
- **Alternative Units**: 
  - Kilometres per hour (km h⁻¹) - multiply by 3.6
  - Knots (kt) - multiply by 1.944
  - Miles per hour (mph) - multiply by 2.237
- **Typical Range**: -60 to +60 m s⁻¹; extremes can exceed ±90 m s⁻¹

## Applications in Climate Research

### Wind Energy Industry
The 100-metre level is critical for modern wind energy:
- **Hub height**: Most utility-scale turbines (2-5 MW) have hub heights of 80-120 metres
- **Power production**: Wind speed at hub height determines actual power output
- **Resource assessment**: 100-m winds better represent available wind resource than surface winds
- **Wake effects**: Turbine interactions occur at hub height
- **Wind farm layout optimization**: Using 100-m wind patterns

### Wind Shear Analysis
Comparison of 100-m and 10-m winds quantifies vertical shear:
- **Shear exponent**: α = ln(U₁₀₀/U₁₀)/ln(100/10)
- Stability indicator (stable: high shear; unstable: low shear)
- Turbine loading and fatigue assessment
- Power production optimization

### Large-Scale Transport
Upper surface layer winds at 100 m affect:
- Long-range pollutant transport (elevated above immediate surface)
- Dust and aerosol dispersion from tall stacks
- Bird and aircraft collision risk assessment
- Drone operation safety altitude

### Boundary Layer Studies
The 100-metre wind characterizes:
- Surface layer to Ekman layer transition
- Diurnal evolution of boundary layer structure
- Low-level jet formation and characteristics
- Mechanical turbulence generation

### Offshore Wind Energy
Over oceans, 100-metre winds are particularly important:
- Less roughness → stronger winds → higher wind shear
- Consistent wind resources
- Offshore wind farm development
- Marine wind climate characterization

## Related Variables
- **100m_v_component_of_wind**: Meridional component; together define complete horizontal wind vector at 100 m
- **10m_u_component_of_wind**: Surface wind for shear calculations
- **10m_wind_speed**: Surface wind magnitude
- **surface_pressure**: Drives horizontal pressure gradient force
- **mean_sea_level_pressure**: Large-scale pressure pattern driving flow

## Mathematical Relationships
- **Wind Speed at 100 m**: WS₁₀₀ = √(U₁₀₀² + V₁₀₀²)
- **Wind Direction**: θ = arctan2(U, V)
- **Wind Shear**: U₁₀₀/U₁₀ ≈ (100/10)^α where α is shear exponent (typically 0.1-0.4)
- **Power Law Profile**: U(z) = Uᵣₑ(z/zᵣₑ)^α
- **Logarithmic Profile**: U(z) = (u*/κ) × ln(z/z₀) where u* is friction velocity, κ ≈ 0.4, z₀ is roughness length

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: 100 metres above surface (diagnostic level)
- **Availability**: 1940 to present

## Quality Considerations
- **Diagnostic extrapolation**: 100-m winds are diagnosed from lower model levels, not directly simulated
- **Topographic effects**: Complex terrain creates 3D flow not captured in vertical profile assumptions
- **Coastal transitions**: Rapid changes in roughness at coastlines
- **Stability dependence**: Profile extrapolation sensitive to atmospheric stability
- **Temporal variability**: Can be higher at 100 m than at 10 m due to reduced surface damping

## Physical Context

### Vertical Wind Profile
Wind speed increases with height following:

**Neutral Atmosphere (typical daytime over land):**
- Power law with α ≈ 0.15
- U₁₀₀/U₁₀ ≈ 1.4

**Stable Atmosphere (typical nighttime):**
- Stronger shear, α ≈ 0.3-0.5
- U₁₀₀/U₁₀ ≈ 1.6-2.0

**Unstable Atmosphere (strong surface heating):**
- Weaker shear, α ≈ 0.05-0.1
- U₁₀₀/U₁₀ ≈ 1.1-1.2

### Low-Level Jets
Nighttime low-level jets often peak near 100-500 m:
- Formed by inertial oscillation after daytime mixing ceases
- Supergeostrophic wind speeds
- Important for wind energy (high wind speeds at turbine height)
- Agricultural implications (insect transport, disease spread)

### Diurnal Variation
The 100-metre wind often shows different diurnal cycle than surface:
- **Daytime**: Strong coupling to surface; both levels similar
- **Nighttime**: Decoupling allows 100-m wind to remain strong while 10-m wind weakens
- **Nocturnal acceleration**: 100-m winds often maximum at night in some regions

## Practical Interpretation for Wind Energy
- **U₁₀₀ < 3 m s⁻¹**: Below cut-in speed; no power production
- **U₁₀₀ 3-4 m s⁻¹**: Cut-in range; turbines begin operation
- **U₁₀₀ 4-12 m s⁻¹**: Partial power; output increases with cube of wind speed
- **U₁₀₀ 12-15 m s⁻¹**: Rated wind speed; maximum power output
- **U₁₀₀ 15-25 m s⁻¹**: Rated power maintained
- **U₁₀₀ > 25 m s⁻¹**: Cut-out; turbines shut down for safety

## Comparison with 10-Metre Wind
Key differences:
1. **Magnitude**: 100-m winds typically 30-50% stronger than 10-m
2. **Variability**: Less influenced by local surface heterogeneity
3. **Diurnal cycle**: Different phase and amplitude
4. **Gusts**: Smoother flow at 100 m
5. **Direction**: May differ from surface wind, especially in stable conditions

## Climate Change Context
Projected changes in 100-metre winds:
- **Wind energy resource**: Regional changes affecting renewable energy potential
- **Jet stream shifts**: Affecting upper-level wind patterns
- **Boundary layer height**: Changes affect altitude of wind maximum
- **Offshore resources**: Generally more robust than onshore

## Wind Energy Economic Implications
The difference between 10-m and 100-m winds is economically significant:
- Wind power density at 100 m can be 2-3× that at 10 m
- Modern turbines capture this enhanced resource
- Accurate 100-m wind data essential for project financing
- Underestimation/overestimation of 100-m winds can make/break project viability

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Stull, R. B. (1988). *An Introduction to Boundary Layer Meteorology*. Springer.
3. Emeis, S. (2018). *Wind Energy Meteorology: Atmospheric Physics for Wind Power Generation* (2nd ed.). Springer.
4. Lundquist, J. K., et al. (2019). Costs and consequences of wind turbine wake effects arising from uncoordinated wind energy development. *Nature Energy*, 4(1), 26-34.
