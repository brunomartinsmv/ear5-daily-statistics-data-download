#!/usr/bin/env python3
"""
ERA5 Daily Statistics Data Download Script

This script downloads ERA5 post-processed daily statistics on single levels 
from 1940 to present using the CDS API.

Dataset: derived-era5-single-levels-daily-statistics
URL: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics
"""

import cdsapi
import argparse
import sys
from datetime import datetime


def download_era5_daily_stats(
    variables,
    year_start,
    year_end,
    months=None,
    daily_statistic='daily_mean',
    time_zone='utc+00:00',
    frequency='1_hourly',
    output_file=None,
    area=None
):
    """
    Download ERA5 daily statistics data.
    
    Args:
        variables (list): List of variable names to download
        year_start (int): Start year (1940 onwards)
        year_end (int): End year
        months (list): List of months to download (default: all months)
        daily_statistic (str): Type of daily statistic (default: 'daily_mean')
        time_zone (str): Time zone for daily statistics (default: 'utc+00:00')
        frequency (str): Frequency of the data (default: '1_hourly')
        output_file (str): Output file name (default: auto-generated)
        area (list): Bounding box [N, W, S, E] (default: global)
    """
    
    # Initialize CDS API client
    c = cdsapi.Client()
    
    # Set default months if not provided
    if months is None:
        months = [f"{i:02d}" for i in range(1, 13)]
    
    # Generate years list
    years = [str(year) for year in range(year_start, year_end + 1)]
    
    # Generate output filename if not provided
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"era5_daily_stats_{year_start}_{year_end}_{timestamp}.nc"
    
    # Build the request
    request = {
        'product_type': 'reanalysis',
        'variable': variables,
        'year': years,
        'month': months,
        'daily_statistic': daily_statistic,
        'time_zone': time_zone,
        'frequency': frequency,
    }
    
    # Add area if specified
    if area is not None:
        request['area'] = area
    
    print(f"Starting download of ERA5 daily statistics...")
    print(f"Variables: {', '.join(variables)}")
    print(f"Years: {year_start} to {year_end}")
    print(f"Daily statistic: {daily_statistic}")
    print(f"Output file: {output_file}")
    print(f"\nThis may take some time depending on the amount of data requested...\n")
    
    try:
        c.retrieve(
            'derived-era5-single-levels-daily-statistics',
            request,
            output_file
        )
        print(f"\nDownload complete! Data saved to: {output_file}")
        return True
    except Exception as e:
        print(f"\nError during download: {e}", file=sys.stderr)
        return False


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Download ERA5 daily statistics data from Copernicus Climate Data Store',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download 2m temperature daily mean for 2020-2023
  python download_era5_daily.py --variables 2m_temperature --start-year 2020 --end-year 2023
  
  # Download multiple variables with custom statistic
  python download_era5_daily.py --variables 2m_temperature total_precipitation --start-year 2020 --end-year 2020 --statistic daily_maximum
  
  # Download for specific months and region
  python download_era5_daily.py --variables 2m_temperature --start-year 2020 --end-year 2020 --months 06 07 08 --area 60 -10 50 2
        """
    )
    
    parser.add_argument(
        '--variables',
        nargs='+',
        required=True,
        help='Variable(s) to download (e.g., 2m_temperature, total_precipitation, 10m_u_component_of_wind)'
    )
    
    parser.add_argument(
        '--start-year',
        type=int,
        required=True,
        help='Start year (1940 onwards)'
    )
    
    parser.add_argument(
        '--end-year',
        type=int,
        required=True,
        help='End year'
    )
    
    parser.add_argument(
        '--months',
        nargs='+',
        default=None,
        help='Months to download (01-12). Default: all months'
    )
    
    parser.add_argument(
        '--statistic',
        default='daily_mean',
        choices=['daily_mean', 'daily_minimum', 'daily_maximum', 'daily_spread'],
        help='Daily statistic type (default: daily_mean)'
    )
    
    parser.add_argument(
        '--time-zone',
        default='utc+00:00',
        help='Time zone for daily statistics (default: utc+00:00)'
    )
    
    parser.add_argument(
        '--frequency',
        default='1_hourly',
        choices=['1_hourly', '3_hourly', '6_hourly'],
        help='Frequency of the data (default: 1_hourly)'
    )
    
    parser.add_argument(
        '--output',
        default=None,
        help='Output file name (default: auto-generated)'
    )
    
    parser.add_argument(
        '--area',
        nargs=4,
        type=float,
        metavar=('N', 'W', 'S', 'E'),
        help='Bounding box: North West South East (e.g., 60 -10 50 2)'
    )
    
    args = parser.parse_args()
    
    # Validate years
    if args.start_year < 1940:
        print("Error: Start year must be 1940 or later", file=sys.stderr)
        sys.exit(1)
    
    if args.start_year > args.end_year:
        print("Error: Start year must be less than or equal to end year", file=sys.stderr)
        sys.exit(1)
    
    # Format months if provided
    months = None
    if args.months:
        months = [f"{int(m):02d}" for m in args.months]
    
    # Call download function
    success = download_era5_daily_stats(
        variables=args.variables,
        year_start=args.start_year,
        year_end=args.end_year,
        months=months,
        daily_statistic=args.statistic,
        time_zone=args.time_zone,
        frequency=args.frequency,
        output_file=args.output,
        area=args.area
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
