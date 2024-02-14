FROM condaforge/mambaforge:4.9.2-5 as conda

LABEL maintainer "{user_name}, {user_email}"
# RUN apt-get update && apt-get install -y build-essential libgl1-mesa-glx && \
#     rm -rf /var/lib/apt/lists/*
# ENV NVIDIA_VISIBLE_DEVICES all
# ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

COPY environment-linux-64.lock .
RUN mamba create -p /env "python=3.9" && conda clean -afy

COPY . /pkg
RUN /env/bin/python -m ensurepip
RUN /env/bin/python -m pip install --upgrade pip
RUN conda run -p /env /env/bin/python -m pip install /pkg/

# Keeping the mambaforge image -> 13Gb, using distroless gets down to 8Gb
FROM gcr.io/distroless/base-debian12

COPY --from=conda /env /env
COPY --from=conda /pkg/data /data

ENV PATH="${{PATH}}:/env/bin/"

EXPOSE 80
ENTRYPOINT ["/env/bin/gunicorn", "{package_name}.__main__:server", "server.port=80"]
