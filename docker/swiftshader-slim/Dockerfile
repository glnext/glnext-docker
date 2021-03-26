FROM python:3.9.2
COPY swiftshader/libvk_swiftshader.so /swiftshader/libvk_swiftshader.so
ENV GLNEXT_BACKEND=/swiftshader/libvk_swiftshader.so
RUN python3 -m pip install glnext==0.8.1 --no-binary :all:
