from django.db import models


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body_html = models.TextField(null=True, blank=True)
    vendor = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField()
    handle = models.CharField(max_length=255)
    updated_at = models.DateTimeField()
    published_at = models.DateTimeField(null=True, blank=True)
    template_suffix = models.CharField(max_length=255, null=True, blank=True)
    published_scope = models.CharField(max_length=50)
    tags = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    admin_graphql_api_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Variant(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product,
        related_name='variants',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.IntegerField()
    inventory_policy = models.CharField(max_length=50)
    compare_at_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    option1 = models.CharField(max_length=255, null=True, blank=True)
    option2 = models.CharField(max_length=255, null=True, blank=True)
    option3 = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    taxable = models.BooleanField()
    barcode = models.CharField(max_length=255, null=True, blank=True)
    fulfillment_service = models.CharField(max_length=50)
    grams = models.IntegerField()
    inventory_management = models.CharField(
        max_length=50, null=True, blank=True)
    requires_shipping = models.BooleanField()
    sku = models.CharField(max_length=255, null=True, blank=True)
    weight = models.FloatField()
    weight_unit = models.CharField(max_length=10)
    inventory_item_id = models.BigIntegerField()
    inventory_quantity = models.IntegerField()
    old_inventory_quantity = models.IntegerField()
    admin_graphql_api_id = models.CharField(max_length=255)
    image_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.price}"


class Option(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product,
        related_name='options',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    position = models.IntegerField()
    values = models.JSONField()

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    alt = models.CharField(max_length=255, null=True, blank=True)
    position = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    admin_graphql_api_id = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    src = models.URLField()
    variant_ids = models.JSONField()

    def __str__(self):
        return self.src


class MainImage(models.Model):
    product = models.OneToOneField(
        Product,
        related_name='main_image',
        on_delete=models.CASCADE
    )
    image = models.OneToOneField(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"Main image for {self.product.title}"


class Address(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_id = models.BigIntegerField()
    company = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=10)
    country_name = models.CharField(max_length=255)
    default = models.BooleanField()

    def __str__(self):
        return f"{self.province}, {self.country}"


class EmailMarketingConsent(models.Model):
    state = models.CharField(max_length=50)
    opt_in_level = models.CharField(max_length=50)
    consent_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.state


class SmsMarketingConsent(models.Model):
    state = models.CharField(max_length=50)
    opt_in_level = models.CharField(max_length=50)
    consent_updated_at = models.DateTimeField(null=True, blank=True)
    consent_collected_from = models.CharField(
        max_length=50, null=True, blank=True)

    def __str__(self):
        return self.state


class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    orders_count = models.IntegerField()
    state = models.CharField(max_length=50)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    last_order_id = models.BigIntegerField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    verified_email = models.BooleanField()
    multipass_identifier = models.CharField(
        max_length=255, blank=True, null=True)
    tax_exempt = models.BooleanField()
    tags = models.TextField(blank=True, null=True)
    last_order_name = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=10)
    addresses = models.ManyToManyField(Address, related_name='customers')
    tax_exemptions = models.JSONField(blank=True, null=True)
    email_marketing_consent = models.OneToOneField(
        EmailMarketingConsent, on_delete=models.CASCADE, null=True, blank=True)
    sms_marketing_consent = models.OneToOneField(
        SmsMarketingConsent, on_delete=models.CASCADE, null=True, blank=True)
    admin_graphql_api_id = models.CharField(max_length=255)
    default_address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name='default_for_customer',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Customer {self.id} - {self.state}"


class MoneySet(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency_code = models.CharField(max_length=10)


class TaxLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.FloatField()
    title = models.CharField(max_length=100)
    price_set_shop = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="tax_shop_money")
    price_set_presentment = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="tax_presentment_money")
    channel_liable = models.BooleanField(default=False)


class LineItem(models.Model):
    admin_graphql_api_id = models.CharField(max_length=255)
    current_quantity = models.IntegerField()
    fulfillable_quantity = models.IntegerField()
    fulfillment_service = models.CharField(max_length=50)
    fulfillment_status = models.CharField(max_length=50, null=True, blank=True)
    gift_card = models.BooleanField()
    grams = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_set_shop = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="line_item_shop_money")
    price_set_presentment = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="line_item_presentment_money")
    product_exists = models.BooleanField()
    product_id = models.BigIntegerField()
    quantity = models.IntegerField()
    requires_shipping = models.BooleanField()
    sku = models.CharField(max_length=50, blank=True)
    taxable = models.BooleanField()
    title = models.CharField(max_length=255)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount_set_shop = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="line_item_discount_shop_money")
    total_discount_set_presentment = models.OneToOneField(MoneySet, on_delete=models.CASCADE, related_name="line_item_discount_presentment_money")
    vendor = models.CharField(max_length=255)


class ClientDetails(models.Model):
    accept_language = models.CharField(max_length=50, null=True, blank=True)
    browser_height = models.IntegerField(null=True, blank=True)
    browser_ip = models.GenericIPAddressField()
    browser_width = models.IntegerField(null=True, blank=True)
    session_hash = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.TextField()


class Order(models.Model):
    id = models.BigIntegerField(primary_key=True)
    admin_graphql_api_id = models.CharField(max_length=255)
    app_id = models.BigIntegerField()
    browser_ip = models.GenericIPAddressField()
    buyer_accepts_marketing = models.BooleanField()
    cancel_reason = models.CharField(max_length=255, null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cart_token = models.CharField(max_length=255, null=True, blank=True)
    checkout_id = models.BigIntegerField()
    checkout_token = models.CharField(max_length=255)
    client_details = models.OneToOneField(
        ClientDetails, on_delete=models.CASCADE, null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    confirmation_number = models.CharField(max_length=50)
    confirmed = models.BooleanField()
    created_at = models.DateTimeField()
    currency = models.CharField(max_length=10)
    current_subtotal_price = models.DecimalField(
        max_digits=10, decimal_places=2)
    current_subtotal_price_set_shop = models.OneToOneField(
        MoneySet, on_delete=models.CASCADE,
        related_name="current_subtotal_shop_money")
    current_subtotal_price_set_presentment = models.OneToOneField(
        MoneySet, on_delete=models.CASCADE,
        related_name="current_subtotal_presentment_money")
    current_total_discounts = models.DecimalField(
        max_digits=10, decimal_places=2)
    current_total_discounts_set_shop = models.OneToOneField(
        MoneySet, on_delete=models.CASCADE,
        related_name="current_discount_shop_money")
    current_total_discounts_set_presentment = models.OneToOneField(
        MoneySet, on_delete=models.CASCADE,
        related_name="current_discount_presentment_money")
    current_total_price = models.DecimalField(
        max_digits=10, decimal_places=2)
    fulfillment_status = models.CharField(blank=True)


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country_code = models.CharField(max_length=10)
    country_name = models.CharField(max_length=100)
    province_code = models.CharField(max_length=10)
    legacy = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin_graphql_api_id = models.CharField(max_length=255)
    localized_country_name = models.CharField(max_length=100)
    localized_province_name = models.CharField(max_length=100)
