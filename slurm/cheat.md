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

Show all qos-es on the system and their priorities:
```
$ sacctmgr show qos format=name,priority
```

Show estimated start time of a Slurm job:
```
$ squeue -j 12345 --start
```

Get Slurm logs that can be grepped for interesting data:
```
$ sacct -S 2019-12-16 -E 2020-01-20 -X --format=jobid,user,account,partition,qos,alloccpus,nnodes,reqmem
```

Workaround if `sacct` truncates job names:
```
$ sacct --format="JobID,JobName%30"
```

Get a list of slurm hostnames which does not need a regex unwrap:
```
$ scontrol show hostnames $SLURM_JOB_NODELIST
```
