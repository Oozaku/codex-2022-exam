package ex01


fun isCnpjValid (cnpj: String): Boolean {
    // Cleaning cnpj from non-number characters and convert char to int
    val cleanCnpj = cnpj
        .filter { it.isDigit() }
        .map { Character.getNumericValue(it) }

    val coef1 = listOf(
        5, 4, 3, 2, 9,
        8, 7, 6, 5, 4,
        3, 2, 0, 0
    )
    val coef2 = listOf(
        6, 5, 4, 3, 2,
        9, 8, 7, 6, 5,
        4, 3, 2, 0
    )

    // Calculate valid1 and valid2 and CNPJ is valid
    // only if they are equal to the last two numbers of cnpj
    var valid1 = 0
    var valid2 = 0
    for (idx in cleanCnpj.indices) {
        valid1 += cleanCnpj[idx] * coef1[idx]
        valid2 += cleanCnpj[idx] * coef2[idx]
    }
    valid1 = 11 - valid1 % 11
    valid1 = if (valid1 >= 10) { 0 } else { valid1 }
    valid2 = 11 - valid2 % 11
    valid2 = if (valid2 >= 10) { 0 } else { valid2 }

    return valid1 == cleanCnpj[12] && valid2 == cleanCnpj[13]
}

fun main (args: Array<String>) {
    val cnpj = args[0]
    if (isCnpjValid(cnpj))
        println("$cnpj is valid!")
    else
        println("$cnpj is not valid!")
}
