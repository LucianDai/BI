/*
   记录不同角色的权限列表
 */
const menu = {
    list() {
        return [
            {"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员"},
            {"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"用户"}
        ]
    }
}
export default menu;
