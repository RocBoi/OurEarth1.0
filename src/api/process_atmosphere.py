import xarray as xr

dataset = xr.open_dataset("data/raw/atmosphere_20260305.nc")

print(dataset)
