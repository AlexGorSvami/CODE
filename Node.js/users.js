function stringfy(user){
  const firstName = capitalize(user.name.first)
  const lastName = capitalize(user.name.last)
  return `${user.name.title} ${firstName} ${lastName}, ${user.email}`
}

function capitalize(str) {
  if (typeof str !== 'string') {
    return ''
  }

  const firstLetter = str.charAt(0).toUpperCase()
  return `${firstLetter}${str.slice(1)}`
}

module.exports = { stringfy }

