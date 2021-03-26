# glnext-docker

```
docker run --rm -it docker.pkg.github.com/glnext/glnext/glnext:swiftshader python3 -c "import glnext; print(glnext.info())"
```

```
docker build -t example examples/image-processing && docker run --rm -it -p 5000:5000 -e PORT=5000 example
```

```Dockerfile
FROM docker.pkg.github.com/glnext/glnext/glnext:swiftshader
```
