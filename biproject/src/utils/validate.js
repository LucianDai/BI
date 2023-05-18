/**
 * 邮箱
 * @param {*} s
 */
export function isEmail(s) {
  return /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(s)
}

/**
 * 手机号码
 * @param {*} s
 */
export function isMobile(s) {
  return /^1[0-9]{10}$/.test(s)
}

/**
 * 电话号码
 * @param {*} s
 */
export function isPhone(s) {
  return /^([0-9]{3,4}-)?[0-9]{7,8}$/.test(s)
}

/**
 * URL地址
 * @param {*} s
 */
export function isURL(s) {
  return /^http[s]?:\/\/.*/.test(s)
}

/**
 * 匹配数字，可以是小数，不可以是负数,可以为空
 * @param {*} s 
 */
export function isNumber(s) {
  return /(^-?[+-]?([0-9]*\.?[0-9]+|[0-9]+\.?[0-9]*)([eE][+-]?[0-9]+)?$)|(^$)/.test(s);
}
/**
 * 匹配整数，可以为空
 * @param {*} s 
 */
export function isIntNumer(s) {
  return /(^-?\d+$)|(^$)/.test(s);
}
/**
 * 身份证校验
 */
export function checkIdCard(idcard) {
  const regIdCard = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
  if (!regIdCard.test(idcard)) {
    return false;
  } else {
    return true;
  }
}

export function checkPassword(pwd) {
  var modes = 0;
  //正则表达式验证符合要求的
  if (pwd.length < 1) return modes;
  if (/\d/.test(pwd)) modes++; //数字
  if (/[a-z]/.test(pwd)) modes++; //小写
  if (/[A-Z]/.test(pwd)) modes++; //大写
  if (/\W/.test(pwd)) modes++; //特殊字符
  // console.log("modes:", pwd.length, modes)
  //逻辑处理
  switch (modes) {
    case 1:
      return 1;
    case 2:
      return 2;
    case 3:
    case 4:
      return pwd.length < 4 ? 3 : 4;
  }
  return modes;
}


