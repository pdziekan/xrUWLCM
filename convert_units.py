def convert_units(ds):
    var_units = {
        "ra" : (1e3, "g/kg"),
        "rl" : (1e3, "g/kg"),
        "rt" : (1e3, "g/kg"),
        "rc" : (1e3, "g/kg"),
        "ri" : (1e3, "g/kg"),
        "r_i" : (1e3, "g/kg"),
        "rr" : (1e3, "g/kg"),
        "ria" : (1e3, "g/kg"),
        "rib" : (1e3, "g/kg"),
        "rv" : (1e3, "g/kg"),
        "lwp" : (1e3, "rg/m$^2$"),
        "cwp" : (1e3, "rg/m$^2$"),
        "rwp" : (1e3, "rg/m$^2$"),
        "all_r_mean" : (1e6, 'r$\mu $m'),
        "all_r_sigma" : (1e6, 'r$\mu $m'),
        "cloud_r_mean" : (1e6, 'r$\mu $m'),
        "cloud_r_sigma" : (1e6, 'r$\mu $m'),
        "rain_r_mean" : (1e6, 'r$\mu $m'),
        "rain_r_sigma" : (1e6, 'r$\mu $m'),
        "na" : (1e-6, '1/mg'),
        "nc" : (1e-6, '1/mg'),
        "nr" : (1e-6, '1/mg'),
        "ni" : (1e-6, '1/mg'),
        "ra" : (1e3, "g/kg"),
        "all_r_m6" : (1e18, r"mm$^6$/m$^3$"),
    }

    for var, (m, u) in var_units.items():
        try:
            ds[var] *= m
            ds[var].attrs["units"] = u
        except:
            pass
            
    ds = ds.assign_coords(t=ds.t/3600.)
    ds.t.attrs["units"] = "h"
    ds.t.attrs["long_name"] = "time"
    
    return ds