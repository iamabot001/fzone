# F95zone Game Tracker

A simple tool to download watchlist from your account and monitor games


### Usage
>**`python -m f95zone [options]`**
    
**Available options:**
>```
>-f           force update local database
>-u          update watchlist from server
>-e          export watchlist and game data to json
>-h          to view help
>```

>```
>-usr      Username for logging in (optional)
>-pass    password for logging in (optional)
>```
>*Recommended Usage:* 
>
> --  *username: provide via arguments*
>
> -- *password: do not provide \
 (prompt to enter when required)*
### Note
- The path is `$HOME/.cache/f95zone` which may evaluate differently depending
on your environment and operating system
- If no option is supplied the current tracked games data is 
printed to the screen
- Your username and password are required to access your watchlist and
are never stored
- `getpass` module is used to safely get the password from the terminal 
without echoing the password to the screen, in case it fails a warning
is displayed
- If no username and password are provided urls can not be scrapped
- Password can be provided as an argument to automate the script but it may be logged in the shell history


### Installation

- Clone this repo and create a package \
 `python setup.py bist_wheel`
- install it with `pip install --user *.whl`

**\[OR\]**

- Packaged wheel files are available in the release section
  - `pip install --user *.whl`



#### Todo
- adding installed games tracker
- installed vs available version comparison
