import argparse
from shopify_scripts.product import gestionar_productos, gestionar_pedidos, gestionar_inventarios
import environ


def main():
    env = environ.Env()
    SHOPIFY_API_KEY = env("SHOPIFY_API_KEY")  # noqa
    SHOPIFY_PASSWORD = env("SHOPIFY_PASSWORD")  # noqa
    SHOPIFY_STORE = env("SHOPIFY_STORE")  # noqa
    BASE_URL = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_PASSWORD}@{SHOPIFY_STORE}.myshopify.com/admin/api/2023-01"  # noqa
    """
    Función principal para ejecutar scripts relacionados con Shopify.
    """
    parser = argparse.ArgumentParser(
        description="Scripts para gestionar la API de Shopify."
    )
    parser.add_argument(
        "accion",
        choices=["productos", "pedidos", "inventarios"],
        help="Selecciona la acción que deseas realizar: productos, pedidos o inventarios.",  # noqa
    )
    parser.add_argument(
        "--filtro",
        help="Filtro opcional para la acción seleccionada (por ejemplo, estado, forma de pago, ubicación, etc.).",  # noqa
        required=False,
    )
    args = parser.parse_args()

    if args.accion == "productos":
        gestionar_productos(args.filtro)
    elif args.accion == "pedidos":
        gestionar_pedidos(args.filtro)
    elif args.accion == "inventarios":
        gestionar_inventarios(args.filtro)
    else:
        print("Acción no reconocida. Usa --help para ver las opciones disponibles.")  # noqa


if __name__ == "__main__":
    main()
