docker volume rm $(docker volume ls -qf dangling=true) 2>/dev/null
