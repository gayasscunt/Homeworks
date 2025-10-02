import importlib, inspect, pkgutil

def first_line(s):
    if not s:
        return ''
    return s.strip().splitlines()[0][:200]

def inspect_module(mod, max_items=30):
    results = []
    members = inspect.getmembers(mod, lambda x: inspect.isfunction(x) or inspect.isclass(x))
    members = sorted(members, key=lambda t: t[0])[:max_items]
    for name, obj in members:
        kind = "class" if inspect.isclass(obj) else "function"
        sig = ""
        try:
            sig = str(inspect.signature(obj))
        except Exception:
            sig = ""
        doc = inspect.getdoc(obj) or ""
        results.append({
            "name": name,
            "type": kind,
            "signature": sig,
            "doc_first_line": first_line(doc),
            "doc_len": len(doc)
        })
    return results

def list_submodules(package_name):
    package = importlib.import_module(package_name)
    submodules = []
    if hasattr(package, "__path__"):
        submodules = [name for _, name, _ in pkgutil.iter_modules(package.__path__)]
    return submodules

def introspect_library(lib_name, important_modules = None, max_items = 30):
    lib = importlib.import_module(lib_name)
    results = {
        "top_level": sorted([a for a in dir(lib) if not a.startswith("_")]),
        "submodules": list_submodules(lib_name),
        "modules_info": {}
    }

    if not important_modules:
        important_modules = [lib_name]

    for mod_name in important_modules:
        try:
            mod = importlib.import_module(f"{lib_name}.{mod_name}") if mod_name != lib_name else lib
            results["modules_info"][mod_name] = inspect_module(mod, max_items=max_items)
        except ImportError:
            continue
    return results
