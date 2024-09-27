FROM mariadb:10.4

# Copy additional configuration
COPY custom.cnf /etc/mysql/conf.d/custom.cnf

# Change permissions for the configuration directory
RUN chmod 777 -R /etc/mysql/conf.d/

# Default command to run when the container starts
CMD ["mysqld", "--default-authentication-plugin=mysql_native_password", "--sql_mode="]