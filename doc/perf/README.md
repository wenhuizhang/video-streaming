# Perf

```
$ perf record -o xxx.log -a -g fp  ${cmd}
// replace ${cmd} with you redis command
$ perf record -o xxx.log -a -g fp  ls 
Then 
$ perf report -i xxx.log 
```
