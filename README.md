# ERA5 Data Download

Scripts to download ERA5 post-processed daily statistics on single levels from 1940 to present using the Copernicus Climate Data Store (CDS) API.

## Dataset Information

This repository provides tools to download data from the **ERA5 post-processed daily statistics on single levels** dataset:
- **Dataset ID**: `derived-era5-single-levels-daily-statistics`
- **URL**: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics
- **Temporal Coverage**: 1940 to present
- **Spatial Coverage**: Global
- **Variables**: Temperature, precipitation, wind, pressure, and many more meteorological variables

## Prerequisites

### 1. Python Environment
- Python 3.6 or higher
- pip package manager

### 2. CDS API Account
Before using these scripts, you need to:

1. **Register** for a free account at the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)
2. **Accept the terms and conditions** for the ERA5 daily statistics dataset at:
   https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics
3. **Get your API credentials**:
   - Login to CDS
   - Go to https://cds.climate.copernicus.eu/how-to-api
   - Copy your UID and API key

### 3. Configure API Credentials

Create a file `~/.cdsapirc` (in your home directory) with your credentials:

```
url: https://cds.climate.copernicus.eu/api
key: UID:API-KEY
```

Replace `UID` with your user ID and `API-KEY` with your actual API key.

Alternatively, copy the example file and edit it:
```bash
cp .cdsapirc.example ~/.cdsapirc
# Edit ~/.cdsapirc with your credentials
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/brunomartinsmv/ear5-data-download.git
cd ear5-data-download
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Command-Line Usage

The main script `download_era5_daily.py` provides a command-line interface for downloading ERA5 data:

```bash
python download_era5_daily.py --variables VARIABLE [VARIABLE ...] --start-year YEAR --end-year YEAR [OPTIONS]
```

### Required Arguments

- `--variables`: One or more variables to download (see Available Variables section)
- `--start-year`: Start year (1940 or later)
- `--end-year`: End year

### Optional Arguments

- `--months`: Specific months to download (01-12). Default: all months
- `--statistic`: Daily statistic type. Choices: `daily_mean`, `daily_minimum`, `daily_maximum`, `daily_spread`. Default: `daily_mean`
- `--time-zone`: Time zone for daily statistics. Default: `utc+00:00`
- `--frequency`: Frequency of the data. Choices: `1_hourly`, `3_hourly`, `6_hourly`. Default: `1_hourly`
- `--output`: Output file name. Default: auto-generated with timestamp
- `--area`: Bounding box for regional data: `N W S E` (North West South East coordinates)

### Examples

#### Example 1: Download 2m temperature for recent years
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 2020 \
    --end-year 2023 \
    --output temp_2020_2023.nc
```

#### Example 2: Download multiple variables
```bash
python download_era5_daily.py \
    --variables 2m_temperature total_precipitation 10m_u_component_of_wind \
    --start-year 2022 \
    --end-year 2022
```

#### Example 3: Download maximum temperature for summer months
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 2020 \
    --end-year 2023 \
    --months 06 07 08 \
    --statistic daily_maximum
```

#### Example 4: Download data for a specific region (Europe)
```bash
python download_era5_daily.py \
    --variables 2m_temperature total_precipitation \
    --start-year 2023 \
    --end-year 2023 \
    --area 71 -25 35 40
```

#### Example 5: Download historical data from 1940s
```bash
python download_era5_daily.py \
    --variables 2m_temperature \
    --start-year 1940 \
    --end-year 1945
```

#### Example 6: Download variables for evapotranspiration analysis (Cuiaba, Brazil)
```bash
python download_era5_daily.py \
    --variables 2m_temperature 2m_dewpoint_temperature 10m_u_component_of_wind 10m_v_component_of_wind surface_net_solar_radiation surface_pressure total_precipitation total_evaporation \
    --start-year 2020 \
    --end-year 2023 \
    --area -13.6 -58.1 -17.6 -54.1 \
    --output era5_evapotranspiration_cuiaba_2020_2023.nc
```

This downloads all variables needed for evapotranspiration analysis using methods like Penman-Monteith or FAO-56.

### Using the Python API

You can also use the download function directly in your Python scripts:

```python
from download_era5_daily import download_era5_daily_stats

# Download 2m temperature for 2020-2023
download_era5_daily_stats(
    variables=['2m_temperature'],
    year_start=2020,
    year_end=2023,
    daily_statistic='daily_mean',
    output_file='temperature_data.nc'
)
```

See `examples.py` for more detailed usage examples.

## Available Variables

Common variables include:
- `2m_temperature` - 2 metre temperature
- `total_precipitation` - Total precipitation
- `10m_u_component_of_wind` - 10 metre U wind component
- `10m_v_component_of_wind` - 10 metre V wind component
- `surface_pressure` - Surface pressure
- `mean_sea_level_pressure` - Mean sea level pressure
- `2m_dewpoint_temperature` - 2 metre dewpoint temperature
- `sea_surface_temperature` - Sea surface temperature

For a complete list of available variables, visit:
https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics

### Variable Documentation

For detailed scientific documentation on each ERA5 variable, including physical descriptions, applications, units, and references, see:
- **[docs/variables_documentation/](docs/variables_documentation/)** - Comprehensive PhD-level documentation for all variables

Each variable is documented with:
- Scientific description and physical context
- Units and typical value ranges
- Applications in climate research
- Mathematical relationships and equations
- Quality considerations and limitations
- Key scientific references

### Evapotranspiration Analysis

For a detailed guide on downloading and analyzing evapotranspiration data, including variable descriptions and calculation methods, see:
- **[docs/EVAPOTRANSPIRATION_GUIDE.md](docs/EVAPOTRANSPIRATION_GUIDE.md)** - Comprehensive guide for ET analysis with Cuiaba example

## Output Format

Downloaded data is saved in NetCDF format (`.nc` files), which can be read with:
- Python: `xarray`, `netCDF4`, `pandas`
- R: `ncdf4`, `raster`
- MATLAB: built-in `ncread` function
- Other tools: CDO, NCO, Panoply

### Reading Downloaded Data with Python

```python
import xarray as xr

# Open the downloaded file
ds = xr.open_dataset('era5_daily_stats_2020_2023.nc')

# Explore the data
print(ds)

# Access a specific variable
temperature = ds['t2m']  # or the variable name in the file

# Plot the data (requires matplotlib)
temperature.isel(time=0).plot()
```

## Notes and Best Practices

1. **Download Size**: ERA5 data files can be very large. Start with small requests (e.g., one year, one variable) to test your setup.

2. **Processing Time**: The CDS API may queue your request. Large downloads can take considerable time to process on the server side.

3. **Rate Limits**: The CDS API has rate limits. Avoid making too many simultaneous requests.

4. **Storage**: Ensure you have sufficient disk space for the downloaded data.

5. **Data Usage**: Please cite the ERA5 dataset in any publications:
   > Hersbach, H., et al. (2020): ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS).

## Troubleshooting

### Authentication Error
- Verify your `~/.cdsapirc` file is correctly formatted
- Check that you've accepted the dataset terms and conditions
- Ensure your API key is valid

### Connection Timeout
- Check your internet connection
- The CDS servers may be experiencing high load; try again later

### Invalid Parameter Error
- Verify variable names are correct (check the dataset documentation)
- Ensure year range is valid (1940 onwards)
- Check that month format is correct (01-12)

## License

This repository contains scripts for downloading ERA5 data. The scripts themselves are provided as-is for use with the Copernicus Climate Data Store. Please refer to the [Copernicus License](https://cds.climate.copernicus.eu/disclaimer-privacy) for terms regarding the ERA5 data itself.

## Repository Structure

```
.
├── download_era5_daily.py         # Main download script with CLI
├── examples.py                    # Example usage scripts
├── requirements.txt               # Python dependencies
├── .cdsapirc.example             # Example API configuration file
├── docs/                         # Documentation
│   ├── EVAPOTRANSPIRATION_GUIDE.md    # Guide for ET analysis
│   └── variables_documentation/       # Detailed variable docs
│       ├── README.md                  # Variables documentation index
│       ├── 2m_temperature.md          # Temperature documentation
│       ├── total_precipitation.md     # Precipitation documentation
│       └── ...                        # Other variable docs
└── README.md                     # This file
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Resources

- [CDS API Documentation](https://cds.climate.copernicus.eu/how-to-api)
- [ERA5 Daily Statistics Dataset](https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics)
- [ERA5 Documentation](https://confluence.ecmwf.int/display/CKB/ERA5)
- [cdsapi Python Package](https://pypi.org/project/cdsapi/)
