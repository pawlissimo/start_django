FROM postgres:10.3

# Run the rest of the commands as the ``postgres`` user
USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'dockerPassword';" &&\
    createdb -O docker db

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10.3/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/10.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/10.3/main/postgresql.conf

EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/10.3/bin/postgres", "-D", "/var/lib/postgresql/10.3/main", "-c", "config_file=/etc/postgresql/10.3/main/postgresql.conf"]