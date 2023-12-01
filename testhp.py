x= input("Enter Name")
y= input("Enter Age")

print((x.upper+y))
# ..
# Prefixes:
#      xsd: http://www.w3.org/2001/XMLSchema
#      ns0: https://krapancheck.cvlindia.com/Imports
#      ns1: https://krapancheck.cvlindia.com

# Global elements:
     
#      ns1:GetPanStatus(panNo: xsd:string, userName: xsd:string, posCode: xsd:string, password: xsd:string, passKey: xsd:string)
#      ns1:GetPanStatusResponse(GetPanStatusResult: {_value_1: ANY})
#      ns1:GetPassword(password: xsd:string, passKey: xsd:string)
#      ns1:GetPasswordResponse(GetPasswordResult: {_value_1: ANY})

# Global types:
#      xsd:anyType
#      xsd:ENTITIES
#      xsd:ENTITY
#      xsd:ID
#      xsd:IDREF
#      xsd:IDREFS
#      xsd:NCName
#      xsd:NMTOKEN
#      xsd:NMTOKENS
#      xsd:NOTATION
#      xsd:Name
#      xsd:QName
#      xsd:anySimpleType
#      xsd:anyURI
#      xsd:base64Binary
#      xsd:boolean
#      xsd:byte
#      xsd:date
#      xsd:dateTime
#      xsd:decimal
#      xsd:double
#      xsd:duration
#      xsd:float
#      xsd:gDay
#      xsd:gMonth
#      xsd:gMonthDay
#      xsd:gYear
#      xsd:gYearMonth
#      xsd:hexBinary
#      xsd:int
#      xsd:integer
#      xsd:language
#      xsd:long
#      xsd:negativeInteger
#      xsd:nonNegativeInteger
#      xsd:nonPositiveInteger
#      xsd:normalizedString
#      xsd:positiveInteger
#      xsd:short
#      xsd:string
#      xsd:time
#      xsd:token
#      xsd:unsignedByte
#      xsd:unsignedInt
#      xsd:unsignedLong
#      xsd:unsignedShort

# Bindings:
#      Soap11Binding: {https://krapancheck.cvlindia.com}BasicHttpBinding_ICVLRestInquiry

# Service: CVLRestInquiry
#      Port: BasicHttpBinding_ICVLRestInquiry (Soap11Binding: {https://krapancheck.cvlindia.com}BasicHttpBinding_ICVLRestInquiry)
#          Operations:
#             GetPanStatus(panNo: xsd:string, userName: xsd:string, posCode: xsd:string, password: xsd:string, passKey: xsd:string) -> GetPanStatusResult: {_value_1: ANY}
#             GetPassword(password: xsd:string, passKey: xsd:string) -> GetPasswordResult: {_value_1: ANY}