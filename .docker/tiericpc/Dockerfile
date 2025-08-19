FROM vnoj/runtimes-tiericpc

ARG TAG=master

RUN mkdir /judge /problems

# Copy our modified judge-server code instead of downloading from GitHub
COPY . /judge

RUN cd /judge && \
	python3 -m venv --prompt=DMOJ /env && \
	/env/bin/pip3 install cython setuptools && \
	/env/bin/pip3 install -e . && \
	/env/bin/python3 setup.py develop && \
	HOME=~judge . ~judge/.profile && \
	runuser -u judge -w PATH -- /env/bin/dmoj-autoconf -V > /judge-runtime-paths.yml && \
	echo '  crt_x86_in_lib32: true' >> /judge-runtime-paths.yml && \
	/judge/.docker/download_testlib_and_precompile

ENTRYPOINT ["/usr/bin/tini", "--", "/judge/.docker/entry"]
