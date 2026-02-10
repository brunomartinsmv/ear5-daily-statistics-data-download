# Quick Start Guide

Get up and running with ERA5 data downloads in 5 minutes!

## 1. Setup (One-time)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Verify setup
```bash
python check_setup.py
```

### Configure CDS API
1. Register at https://cds.climate.copernicus.eu/
2. Accept terms: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics
3. Get your API key: https://cds.climate.copernicus.eu/how-to-api
4. Create `~/.cdsapirc`:
```
url: https://cds.climate.copernicus.eu/api
key: YOUR_UID:YOUR_API_KEY
```

## 2. Download Data

### Simple download (temperature 2020-2023)
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 2020 \
    --end-year 2023
```

### Multiple variables
```bash
python download_era5_daily.py \
    --variables 2m_temperature total_precipitation \
    --start-year 2022 \
    --end-year 2022
```

### Regional data (Europe)
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 2023 \
    --end-year 2023 \
    --area 71 -25 35 40
```

### Maximum temperature for summer
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 2020 \
    --end-year 2023 \
    --months 06 07 08 \
    --statistic daily_maximum
```

## 3. Read the Data

```python
import xarray as xr

ds = xr.open_dataset('your_file.nc')
print(ds)
```

## Common Variables
- `2m_temperature` - Temperature at 2 meters
- `total_precipitation` - Total precipitation
- `10m_u_component_of_wind` - U wind component at 10m
- `10m_v_component_of_wind` - V wind component at 10m
- `surface_pressure` - Surface pressure
- `mean_sea_level_pressure` - Sea level pressure

## Need Help?
See the full [README.md](README.md) for detailed documentation.
