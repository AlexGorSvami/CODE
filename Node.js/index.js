const data = require('./users.json')
const { stringfy: stringfyUser } = require('./users.js')

data.forEach(user => {
  const formattedUserStr = stringifyUser(user)
  console.log(formattedUserStr)
})
