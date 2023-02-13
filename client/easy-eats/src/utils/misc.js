const jwt = require('jsonwebtoken');

function validateJwt(token) {
    try {
        return jwt.verify(token, process.env.VUE_APP_SECRET)
    } catch (error) {
        throw new Error('Invalid token')
    }
}

export default validateJwt
