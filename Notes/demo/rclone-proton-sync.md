# Rclone proton


```sh
rclone bisync proton:/sync . --verbose --resync
rclone bisync proton:/sync . --verbose
*/10 * * * * cd /home/user/Documents && rclone bisync proton:/sync .
# --log-file /path/to/a/new/cron.log
# --protondrive-replace-existing-draft 
# transfers=16
rclone sync -P -v /home/user/wtv proton:/wtv
rclone mount proton: protonmount --vfs-cache-mode writes --allow-non-empty

```

- Wireguard vs OpenVPN

### Features
- Port forwarding
- kill switch
- netshield 
- Moderate NAT 

### Alt

- Filen 
- Koofr
- Quatrix
- Synology C2
- Leviia
- Onlime
- Telia Sky


### REF
- https://www.reddit.com/r/ProtonVPN/comments/16fu4ku/the_proton_vpn_linux_client_is_now_available_in/
- https://www.reddit.com/r/rclone/comments/1d2pm6p/rclone_blocked_by_proton_drive_it_seems/?share_id=E7Wk9x_YtWoDoTOjBkvSE&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1
- https://www.reddit.com/r/ProtonDrive/comments/1d2m4oe/no_more_rclone_with_drive/
- https://www.reddit.com/r/ProtonDrive/comments/16g53i5/protondrive_with_rclone/