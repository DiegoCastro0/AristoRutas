import psycopg2

try:
    conn = psycopg2.connect(
        dbname='usuarios',
        user='usuario',
        password='usuario123',
        host='localhost'
    )
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS "Login_usuario", "Iniciar_iniciar" CASCADE;')
    conn.commit()
    cur.close()
    conn.close()
    print('✓ Tablas borradas correctamente')
except Exception as e:
    print(f'✗ Error: {e}')
