

# Slurm cheat sheet

Display info about job:
```
$ scontrol show jobid -dd 12345
```

Get time limit of a job:
```
$ sacct -j 12345 --format="Timelimit"
```

Set new time limit for a job (here we extend the job to 4 days):
```
$ scontrol update jobId 12345 TimeLimit=4-00:00:00
```

Un-block a job that is "launch failed requeued held":
```
$ scontrol release 12345
```
