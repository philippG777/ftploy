# ftploy

A simple CLI-tool for deploying applications to ftp-servers without exposing sensitive information like README-files or `.git/`.

It doesn't only work with FTP - You can use it with any mounted directory.

## Usage

Just call `ftploy.py` in the directory where `deploy.json` is located.
The `deploy.json`-file contains the deployment-configuration.

## deploy.json

```json
{
    "source": "dist",
    "dest":   "path/to/mounted/ftp/server",
    "include_file_ext": [
        "php", "xhtml", "html", "js", "css"
    ],
    "include": [
        "robots.txt",
        "easter/egg.txt"
    ],
    "exclude": [
        "init_sql.php",
        "login/test.php"
    ],
    "build": "npm build"
}
```

### source
The source-directory of the code, that should be deployed.

### dest
Path to the mounted FTP-server (or any other mounted directory). Where the source-files should go.

### include_file_ext
Only files with this extensions are copied to the `dest`-directory.

### include
Files that should be transfered to the server, even if they don't have the right file-extension.

### exclude
Files that match the included file-extensions, but **should not be transfered** to the `dest`.

### build
A command that's executed before deployment. For example `npm build`.
