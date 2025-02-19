PcComRastrillo - Bot PcComponentes

Este repositorio contiene un script en Python desarrollado en 2021, durante la escasez global de tarjetas gráficas, para automatizar el proceso de compra en la web de PcComponentes.

💡 Descripción

El script realiza las siguientes funciones:

Web Scraping: Monitoriza el stock de tarjetas gráficas en PcComponentes.

Inicio de Sesión Automático: Realiza login en la cuenta del usuario proporcionada en la configuración.

Compra Automática: Cuando se encuentra el producto indicado, el script añade la tarjeta gráfica al carrito y finaliza la compra de forma automática.

⚡ Requisitos

Python 3.x

Librerías: selenium

Un navegador compatible y el driver correspondiente (por ejemplo, ChromeDriver para Chrome)

⛓ Advertencia

Este script fue creado en un contexto de escasez extrema de componentes y está pensado para uso personal. El uso de bots de compra automatizada puede ir en contra de los términos de servicio de PcComponentes u otras tiendas, por lo que se recomienda usarlo de manera responsable y ética.

💎 ¿Por qué este proyecto?

Durante 2021, conseguir una tarjeta gráfica a precio razonable se convirtió en un desafío debido a la alta demanda y la acción de bots comerciales. Este script nació como una herramienta para nivelar el campo de juego.

📝 Uso

Clonar este repositorio:

git clone https://github.com/hmonra/PcComRastrillo.git
cd PcComRastrillo

Instalar las dependencias:

pip install -r requirements.txt

Configurar las credenciales y parámetros de producto en el archivo de configuración del script.

Ejecutar el script:

python main.py

🔧 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o hacer un pull request para mejorar el código, añadir soporte para otras tiendas o optimizar el proceso de scraping.

📈 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

💡 Nota: PcComponentes puede cambiar su estructura HTML o implementar medidas anti-bots, por lo que el funcionamiento del script no está garantizado a largo plazo.

