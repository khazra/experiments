# Offline experiment utilities

Python 3 and a POSIX shell are required. No utility contacts a network, opens an account, changes credentials or starts a worker.

- `collect-evidence.sh LOCAL_DIRECTORY` prints sorted JSONL path/size/SHA-256 records. It inventories all files, including dotfiles, except the root `.git` directory. It copies no source contents. Filenames themselves can be private: retain an inventory privately until reviewed.
- `sanitize-snapshot.sh LOCAL_DIRECTORY` checks common credentials, multiline key arrays, tokens and payment/contact addresses. It emits detector names and filenames, never matched values. It rejects symlinks, special files and read errors. A clean scan is not complete anonymization; review names, context, images, filenames and unrecognized secrets separately.
- `control.sh status STATE_DIRECTORY` reads a local planning marker without creating a directory. `mark-paused` creates an idempotent marker. **A marker does not stop a worker or establish that an experiment is paused.** A real pause requires stopping every worker/controller and verifying process and remote states.
- `deploy/render-service.py` renders a bounded Linux user-service example to stdout; it installs and starts nothing. See the deployment notes.
- `tests/run.sh` runs offline positive and negative tests using temporary synthetic fixtures, no credentials, network or host access.

Collection and scan operate on a static local tree. Concurrent mutations are outside their integrity guarantee; freeze or copy inputs before use. Hashing a source does not make it safe to publish. No deployment, customer interaction or earning restart is authorized here.
