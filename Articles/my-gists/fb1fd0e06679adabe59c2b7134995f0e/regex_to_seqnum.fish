➜ set -l regex '^\d+-'
  set -l n 100
  ls | while read -l file
          set new_name (printf "%02d-%s" $n (string replace -r $regex "" (basename $file)))
          echo "mv $file $new_name"
          set n (math $n + 1)
  end
