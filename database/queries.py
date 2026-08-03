class IOCQueries:

    GET_ALL = """
        SELECT
            Id,
            Value,
            Type,
            Domain,
            IPv4,
            IPv6,
            Description,
            Source,
            IOCDate,
            CriticalityLevel,
            ConnectionType,
            Origin,
            IsEnabled
        FROM IOC
        ORDER BY IOCDate DESC
    """

    GET_BY_ID = """
        SELECT *
        FROM IOC
        WHERE Id=?
    """

    GET_BY_TYPE = """
        SELECT
            Id,
            Value,
            Type,
            Domain,
            IPv4,
            IPv6
        FROM IOC
        WHERE
            Type=?
            AND IsEnabled=1
        ORDER BY IOCDate DESC
    """

    COUNT = """
        SELECT COUNT(*)
        FROM IOC
    """

    COUNT_IPV4 = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Type='ipv4' AND Origin='API'
    """

    COUNT_IPV6 = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Type='ipv6' AND Origin='API'
    """

    COUNT_DOMAIN = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Type='domain' AND Origin='API'
    """

    COUNT_URL = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Type='url' AND Origin='API'
    """

    COUNT_MANUAL = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Origin='MANUAL'
    """

    EXISTS = """
        SELECT COUNT(*)
        FROM IOC
        WHERE Id=?
    """

    INSERT = """
        INSERT INTO IOC
        (
            Id,
            Value,
            Type,
            Domain,
            IPv4,
            IPv6,
            Description,
            Source,
            IOCDate,
            CriticalityLevel,
            ConnectionType,
            Origin,
            IsEnabled
        )

        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?,?,?,?
        )
    """

    UPDATE = """
        UPDATE IOC

        SET

            Value=?,
            Type=?,
            Domain=?,
            IPv4=?,
            IPv6=?,
            Description=?,
            Source=?,
            IOCDate=?,
            CriticalityLevel=?,
            ConnectionType=?,
            UpdatedAt=GETDATE()

        WHERE Id=?
    """

    UPDATE_MANUAL = """
        UPDATE IOC

        SET

            Value=?,
            Type=?,
            Domain=?,
            IPv4=?,
            IPv6=?,
            UpdatedAt=GETDATE()

        WHERE Id=?
    """

    DELETE = """
        DELETE FROM IOC
        WHERE Id=?
    """

    ENABLE = """
        UPDATE IOC

        SET

            IsEnabled=?,
            UpdatedAt=GETDATE()

        WHERE Id=?
    """

    TRUNCATE = """
        DELETE FROM IOC
    """
