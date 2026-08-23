# 🔍 Pattern Scanner & Detector (Clojure / Multi-Paradigm)

> **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)** Pattern Detection Engine in Python with **ANTLR4** grammar parsing.

---

## 🏛 Architecture Overview

```text
                    ┌─────────────────────────────────────────┐
                    │            Driving Adapters             │
                    │                                         │
                    │   CLI (Typer + Rich)   /   Python API   │
                    └────────────────────┬────────────────────┘
                                         │
                                         ▼
                    ┌─────────────────────────────────────────┐
                    │            Application Layer            │
                    │                                         │
                    │  ScanningService (Use Cases & Pipeline) │
                    └────────────────────┬────────────────────┘
                                         │
                               ┌─────────▼─────────┐
                               │    DOMAIN CORE    │
                               │                   │
                               │  CodeModel        │
                               │  PatternRules     │
                               │  Detection Engine │
                               │  Confidence Model │
                               └─────────┬─────────┘
                                         │
                    ┌────────────────────▼────────────────────┐
                    │               Ports / SPI               │
                    │                                         │
                    │ ParserPort         SourceProviderPort   │
                    │ ResultRepoPort     ReportFormatterPort  │
                    └────────────────────┬────────────────────┘
                                         │
                    ┌────────────────────▼────────────────────┐
                    │             Driven Adapters             │
                    │                                         │
                    │ ANTLR4 Clojure Parser  (Clojure.g4)     │
                    │ FileSystem Source Provider              │
                    │ JSON Result Repository                  │
                    │ Rich Console Report Formatter           │
                    └─────────────────────────────────────────┘
```

---

## 🚀 Key Features & Highlights

1. **Agnostic Domain `CodeModel`:**
   - The domain layer has **zero knowledge** of ANTLR, tokens, grammar files, or AST implementations.
   - Operates on high-level abstractions: `ProtocolModel`, `RecordModel`, `FunctionModel`, `StateModel`, `WatchModel`, `MethodSignature`.

2. **Heuristic Evidence & Confidence Scoring:**
   - Patterns are detected with measurable **confidence scores** (0.0 to 1.0) and an **evidence trail** with weights and source locations.
   - Example:
     ```text
     OBSERVER on state 'system-events' (88% VERY HIGH)
     ├── +50% (WATCHED_STATE) State container 'system-events' is subscribed to via add-watch
     ├── +35% (ADD_WATCH_CALL) Watcher key 'audit-logger' registers callback 'on-system-event-changed'
     └── +25% (OBSERVER_CALLBACK_SIGNATURE) Callback function matches [key ref old-state new-state]
     ```

3. **Pluggable Rule / Specification Pattern (OCP):**
   - Adding a new pattern detection rule requires only implementing the `PatternRule` protocol without modifying core pipelines.

4. **ANTLR4 Clojure Grammar Integration:**
   - Direct integration with official [`Clojure.g4`](https://raw.githubusercontent.com/antlr/grammars-v4/refs/heads/master/clojure/Clojure.g4).
   - Extracts namespaces, protocols, records, types, extensions (`extend-type`/`extend-protocol`), multimethods (`defmulti`/`defmethod`), Ring middleware, atoms, watchers, macros, and closures.

---

## 📐 Supported Design Patterns (17 Detection Rules)

| Pattern Type | Category | Detection Strategy & Heuristics |
|---|---|---|
| **Observer** | Behavioral | Watched `atom`/`ref`/`agent`, `add-watch` calls, 4-arg watcher callbacks `[k r o n]`. |
| **Strategy** | Behavioral | `defmulti` dispatch function + `defmethod` branches, or `defprotocol` with 2+ implementing records. |
| **Decorator** | Structural | Ring-style middleware: functions taking `[handler]` and returning inner closures `(fn [req] ...)`. |
| **Chain of Responsibility** | Behavioral | Pipeline assembly chaining middleware stages using `->`, `->>`, or `comp`. |
| **Template Method** | Behavioral | `with-*` macros/functions encapsulating `try/finally` acquire-release bracket safety. |
| **Command / CQRS** | Behavioral | Multimethod message dispatch on `:type`/`:command`/`:op` and command records. |
| **State / FSM** | Behavioral | State machine transition functions / multimethods on `[state event]`. |
| **Singleton** | Creational | `defonce` with mutable reference container (`atom`, `ref`, `agent`) or memoized lazy delay. |
| **Factory Method** | Creational | Constructor helpers (`make-*`, `create-*`, `build-*`, `new-*`) encapsulating `->Record` or `map->Record`. |
| **Abstract Factory** | Creational | Protocols declaring families of object creation interfaces implemented by concrete factories. |
| **Builder** | Creational | Fluent configuration step functions (`with-*`, `set-*`) modifying accumulator maps/records. |
| **Adapter** | Structural | External protocol extensions (`extend-type`/`extend-protocol`) adapting host/Java types. |
| **Facade** | Structural | High-level API/gateway namespaces aggregating and delegating calls to multiple subsystems. |
| **Proxy** | Structural | Dynamic interop proxies `(proxy [Class] ...)` and deferred access via `delay`/`future`. |
| **Flyweight** | Structural | Shared immutable instances and result caches via `memoize` or interning. |
| **Lifecycle Component** | Architectural | Stuart Sierra `Lifecycle` component protocol with `start` and `stop` lifecycle transitions. |
| **Circular Dependency** | Architectural | Architectural namespace dependency cycle analysis (`A ➔ B ➔ A` loops). |

---

## 🛠 Installation & Setup

Using [`uv`](https://github.com/astral-sh/uv) (recommended):

```bash
# Install dependencies
uv sync

# Run the test suite with coverage
uv run pytest --cov=pattern_detector -v

# Run linter and type checks
uv run ruff check .
uv run mypy src/pattern_detector
```

---

## 💻 CLI Usage

### 1. Scan a Project / Directory
```bash
uv run pattern-detector scan examples/clojure_samples
```

### 2. Filter by Minimum Confidence Threshold
```bash
uv run pattern-detector scan examples/clojure_samples --min-confidence 0.70
```

### 3. Filter by Pattern Type
```bash
uv run pattern-detector scan examples/clojure_samples --pattern strategy --pattern observer
```

### 4. Export Report to JSON
```bash
uv run pattern-detector scan examples/clojure_samples --json report.json
```

### 5. List All Registered Detection Rules
```bash
uv run pattern-detector rules
```

### 6. System & Architecture Info
```bash
uv run pattern-detector info
```

---

## 🐍 Python API Usage

```python
from pattern_detector.bootstrap import create_container
from pattern_detector.ports import ScanOptions

# 1. Initialize DI Container (Hexagonal Composition Root)
container = create_container()
scanner = container.get_scanner()

# 2. Configure scan options
options = ScanOptions(
    min_confidence=0.6,
    enabled_patterns=["strategy", "observer", "decorator"],
)

# 3. Execute scan
report = scanner.scan_path("path/to/clojure/project", options=options)

print(f"Scanned {report.scanned_files_count} files in {report.elapsed_seconds:.3f}s")
print(f"Found {report.total_detections_count} pattern instances:")

for det in report.detections:
    print(f"[{det.level.value}] {det.pattern_type.value} on {det.target_name} ({det.confidence.percentage_str})")
    for ev in det.evidences:
        print(f"   +{int(ev.weight * 100)}% {ev.description}")
```

---

## 📂 Project Directory Structure

```text
src/pattern_detector/
├── domain/                          # Core Domain Layer (Agnostic)
│   ├── value_objects.py             # Location, Confidence, Evidence, PatternType
│   ├── code_model.py                # Protocol, Record, Function, State, Invocations
│   ├── pattern.py                   # Pattern Catalog metadata
│   ├── detection.py                 # Detection and DetectionReport entities
│   ├── rules/                       # Pluggable Specification Rules
│   │   ├── base.py                  # PatternRule Protocol & BasePatternRule
│   │   ├── observer_rule.py
│   │   ├── strategy_rule.py
│   │   ├── decorator_rule.py
│   │   ├── singleton_rule.py
│   │   ├── factory_rule.py
│   │   ├── adapter_rule.py
│   │   └── lifecycle_rule.py
│   └── services/
│       └── pattern_detector.py      # Domain Service coordinating rules
│
├── ports/                           # Ports Layer (Interfaces)
│   ├── inbound.py                   # ScannerPort, DetectorPort, ScanOptions
│   └── outbound.py                  # ParserPort, SourceProviderPort, ResultRepositoryPort, ReportFormatterPort
│
├── application/                     # Application Layer (Use Cases)
│   └── services/
│       └── scanning_service.py      # Scanning pipeline coordinator
│
├── adapters/                        # Adapters Layer (Driven & Driving)
│   ├── inbound/
│   │   └── cli/main.py              # CLI Driving Adapter (Typer + Rich)
│   └── outbound/
│       ├── antlr/                   # ANTLR Clojure Driven Adapter
│       │   ├── generated/           # ANTLR4 generated python lexer & parser
│       │   ├── clojure_ast.py       # S-expression AST intermediate nodes
│       │   ├── clojure_visitor.py   # ANTLR Visitor
│       │   └── clojure_parser_adapter.py # Implements ParserPort
│       ├── filesystem/
│       │   └── file_source_provider.py   # Implements SourceProviderPort
│       └── persistence/
│           ├── json_result_repository.py # Implements ResultRepositoryPort
│           └── console_report_formatter.py # Implements ReportFormatterPort
│
└── bootstrap/                       # Composition Root
    └── container.py                 # Dependency Injection Container
```
