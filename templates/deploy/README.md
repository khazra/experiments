# Inert deployment configuration renderer

`render-service.py` prints a Linux systemd **user service** example; it performs no installation, account change or process launch. It requires a plain absolute path to an operator-supplied runner program, a working directory and a maximum duration of at most five days. It does not read or execute the supplied program.

Example on a future authorized machine:

```sh
python3 templates/deploy/render-service.py --program /path/to/runner --workdir /path/to/work --max-seconds 3600
```

Output disables automatic restarts, sets a duration limit and stops the service control group on termination. Review it before any future installation. User-service configuration is Linux-specific; the offline inventory and scanner are portable Python/POSIX utilities. No production supervisor, notification system or application idempotency is supplied by this small example.

A future launch needs explicit scope, account/AI eligibility, budget, tested alerts, retention covering the window and a pause inventory covering nested/local/remote workers. The future action policy must distinguish delegated routine actions from actions requiring approval. The marker utility is not a kill switch. Passing offline tests is not deployment approval.
