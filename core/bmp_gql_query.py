# Мутация создания заказа
create_order = """
mutation ($input: CreateOrderInput!) {
  createOrder(input: $input) {
    id
    number
    groupStatusCode: statusCode
    statusTitle
    dateCreated
    orderGroupSum
    originalOrderGroupSum
    invoiceUrl
    isMy
    isAwaitingCancellation
    isCancellable
    isRepeatable
    hasDebt
    orders {
      id
      number
      statusCode
      statusTitle
      paymentDetail {
        isComplete
        paymentPartList {
          vendorFormUrl
          lifetime
        }
      }
      paymentMethodCode
      paymentMethodTitle
      paymentMethods(
        supportedPaymentMethodCodes: ["online", "autopayment", "sbp"]  
      ) {
        code
        title
        description
        isActive
        dates
        change {
          code
          value
          currencyCode
        }
      }
      delivery
      deliveryMethodTitle
      comment
      isAgreementAccepted
      coordinates {
        latitude
        longitude
      }
      address
      porch
      floor
      flat
      datetimeFrom
      datetimeTo
      datetimeCreated
      deliveryPrice
      originalDeliveryPrice
      firstname
      lastname
      phone
      email
      isMy
      orderItems {
        id
        productId
        productCode
        amount
        name
        price
        imageId
        isActive
        quant {
          code
          fullName
          shortName
          multiple
          pricePerUnit
          previousPricePerUnit
          unit
          type
          minAmount
          stepAmount
          amountPerQuant
          currency
          unitCode
        }
        orderItemSum
        isCreateReviewAvailable
        isGift
      }
      orderSum
      originalOrderSum
      invoiceUrl
      change {
        code
        value
        currencyCode
      }
      isAwaitingCancellation
      isCancellable
      trackingNumbers
      minDeliveryTime
      maxDeliveryTime
      isPrivateHouse
      customerOrderNumber
      bankCardID
      isRepeatable
      hasDebt
      isCanPayment
      orderGroup {
        id
        isRepeatable
        hasDebt
        orders {
          id
          number
          statusCode
          isAwaitingCancellation
          paymentDetail {
            isComplete
            paymentPartList {
              vendorFormUrl
              lifetime
            }
          }
          bankCardID
        }
      }
    }
  }
}
"""

# Запрос слотов доставки
delivery_slots = """
query ($input: DeliverySlotsRequest!) {
  deliverySlots(input: $input) {
    list {
      title
      deliveryToken
      paymentMethods {
        code
        title
        isActive
        replacementMethods {
          code
          title
        }
      }
      isDefault
      ... on DeliverySlotRegular {
        date
        cost
        priceThreshold
      }
      ... on DeliverySlotNearest {
        date
        cost
        priceThreshold
      }
      ... on DeliverySlotParcel {
        minDeliveryTime
        maxDeliveryTime
      }

      ... on DeliverySlotPickup {
        stock {
          address
          vendorGuid
        }
      }
    }
  }
}
"""

# Мутация изменения продуктов в корзине
update_products_in_cart = """
mutation ($input: UpdateProductsInCartInput!) {
  updateProductsInCart(input: $input) {
    cartGroups(
      input: { supportedPaymentMethods: ["online", "autopayment", "sbp"] }
    ) {
      id
      products {
        id
        code
        name
        description
        amount
        image {
          id
          title
          alt
        }
        itemSum
        isNew
        isHit
        isVkusvill
        isFavorite
        isAvailable
        isSubscribed
        isVeterinaryControl
        quant {
          code
          fullName
          shortName
          multiple
          pricePerUnit
          previousPricePerUnit
          unit
          type
          minAmount
          stepAmount
          amountPerQuant
          currency
          unitCode
        }
        categories {
          id
          name
          code
          treeId
          parentTreeId
        }
        rating
        numberOfRatings
        brand
      }
      agreement {
        id
        number
        activeFrom
        activeTo
        minimalOrderSum
        currency
        agreementGroup {
          code
          name
          isDefault
          deliveryPersonGroupId
        }
      }
      stock {
        id
      }
      deliveryMethods {
        code
        title
        description
        isActive
        priority
        minDeliveryTime
        maxDeliveryTime
      }
      paymentMethods {
        code
        title
        description
        isActive
        dates
        change {
          code
          value
          currencyCode
        }
        replacementMethods {
          code
          title
        }
      }
    }
  }
}
"""


