#!/usr/bin/env python3
"""
Example usage script for ERA5 daily statistics download.

This script demonstrates various use cases for downloading ERA5 data.
Modify the examples below to suit your needs.
"""

from download_era5_daily import download_era5_daily_stats


def example_temperature_recent_years():
    """Download 2m temperature daily mean for recent years (2020-2023)."""
    print("Example 1: Downloading 2m temperature for 2020-2023\n")
    
    download_era5_daily_stats(
        variables=['2m_temperature'],
        year_start=2020,
        year_end=2023,
        daily_statistic='daily_mean',
        output_file='era5_temp_2020_2023.nc'
    )


def example_multiple_variables():
    """Download multiple variables for a single year."""
    print("\nExample 2: Downloading multiple variables for 2022\n")
    
    download_era5_daily_stats(
        variables=[
            '2m_temperature',
            'total_precipitation',
            '10m_u_component_of_wind',
            '10m_v_component_of_wind'
        ],
        year_start=2022,
        year_end=2022,
        daily_statistic='daily_mean',
        output_file='era5_multi_vars_2022.nc'
    )


def example_summer_months_max_temp():
    """Download maximum temperature for summer months."""
    print("\nExample 3: Downloading maximum temperature for summer months 2020-2023\n")
    
    download_era5_daily_stats(
        variables=['2m_temperature'],
        year_start=2020,
        year_end=2023,
        months=['06', '07', '08'],  # June, July, August
        daily_statistic='daily_maximum',
        output_file='era5_temp_max_summer_2020_2023.nc'
    )


def example_regional_data():
    """Download data for a specific region (Europe)."""
    print("\nExample 4: Downloading temperature for Europe (2023)\n")
    
    # Area: [North, West, South, East]
    # Europe bounding box: approximately 71N, -25W, 35N, 40E
    europe_area = [71, -25, 35, 40]
    
    download_era5_daily_stats(
        variables=['2m_temperature', 'total_precipitation'],
        year_start=2023,
        year_end=2023,
        area=europe_area,
        output_file='era5_europe_2023.nc'
    )


def example_historical_data():
    """Download historical data from 1940s."""
    print("\nExample 5: Downloading historical temperature data (1940-1945)\n")
    
    download_era5_daily_stats(
        variables=['2m_temperature'],
        year_start=1940,
        year_end=1945,
        daily_statistic='daily_mean',
        output_file='era5_temp_1940_1945.nc'
    )


def main():
    """
    Main function - uncomment the example you want to run.
    
    NOTE: Before running this script:
    1. Install requirements: pip install -r requirements.txt
    2. Set up your CDS API credentials in ~/.cdsapirc
    """
    
    print("ERA5 Daily Statistics Download Examples")
    print("=" * 50)
    print("\nIMPORTANT: Make sure you have:")
    print("1. Installed cdsapi: pip install -r requirements.txt")
    print("2. Created ~/.cdsapirc with your CDS API credentials")
    print("3. Accepted the terms and conditions at:")
    print("   https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics")
    print("\n" + "=" * 50 + "\n")
    
    # Uncomment ONE of the examples below to run:
    
    # example_temperature_recent_years()
    # example_multiple_variables()
    # example_summer_months_max_temp()
    # example_regional_data()
    # example_historical_data()
    
    print("\nUncomment one of the examples in the script to run it.")


if __name__ == '__main__':
    main()
