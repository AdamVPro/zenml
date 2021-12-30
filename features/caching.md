---
description: Caching takes your pipeline to the next level.
---

# Caching

Machine learning pipelines are rerun many times over throughout their development lifecycle. Prototyping is often a fast and iterative process that benefits a lot from caching. This makes caching a very powerful tool. (Read [our blogpost](https://blog.zenml.io/caching-ml-pipelines/) for more context on the benefits of caching.)

ZenML comes with caching enabled by default. As long as there is no change within a step or upstream from it, the cached outputs of that step will be used for the next pipeline run. This means that whenever there are code or configuration changes affecting a step, the step will be rerun during the next pipeline execution. Currently, the caching does not automatically detect changes within the file system or on external APIs. Make sure to set caching to `False` on steps that depend on external input.

There are multiple ways to take control of when and where caching is used.

### Caching on a Pipeline Level

On a pipeline level the caching policy can easily be set as a parameter within the decorator. If caching is explicitly turned off on a pipeline level, all steps are run without caching, even if caching is set to true for single steps.

```python
@pipeline(enable_cache=False)
def pipeline(....):
    """Pipeline with cache disabled"""
```

### Caching on a Step Level

Caching can also be explicitly turned off at a step level. You might want to turn off caching for steps that take external input (like fetching data from an API/ File IO).

```python
@step(enable_cache=False)
def import_data_from_api(...):
    """Import most up-to-date data from public api"""
    ...
    
@pipeline(enable_cache=True)
def pipeline(....):
    """Pipeline with cache disabled"""
```
