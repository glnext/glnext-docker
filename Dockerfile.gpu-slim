FROM python:3.9.2
RUN wget -qO - https://packages.lunarg.com/lunarg-signing-key-pub.asc | apt-key add - &&\
    wget -qO /etc/apt/sources.list.d/lunarg-vulkan-1.2.170-bionic.list https://packages.lunarg.com/vulkan/1.2.170/lunarg-vulkan-1.2.170-bionic.list &&\
    apt-get update && apt-get install -y libvulkan-dev
RUN python3 -m pip install glnext==0.8.1 --no-binary :all:
