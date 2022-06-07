from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class User(GetTokenHeader):
    def get_me(self):
        """
        :return:class User; 如果想要tcompany_id, 可以使用:
            res.company.id, res = return
        """
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.me()
        data = endpoint(op)
        res = (op + data).me
        return res

    def get_user(self, id):
        """
        获取user基本信息
        @param id : tenant id
        """
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.user(id=id)
        data = endpoint(op)
        res = (op + data).user
        return res

    def roles_info(self, args=None, **kwargs):
        """
        @param args:
        @param kwargs:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.role_list(
            filter=eval(f"{kwargs}")
        )
        if args:
            users_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).role_list
        return res

    def create_user(self, variables):
        """
        create a user
        @param variables:dict
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_role(self, variables):
        """
        @param variables: dict
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_user_list(self,variables):
        """
        获取用户列表数据
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        user_list = op.user_list(filter=variables)
        data = endpoint(op)
        res = (op + data).user_list
        return res

    def enable_users(self, ids: list):
        """
        启用用户
        @param ids:list
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.enable_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).enable_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def disable_users(self, ids: list):
        """
        禁用用户
        @param ids : list
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.disable_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).disable_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_users(self, ids: list):
        """
        删除用户
        @param ids: list,用户id集合
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def reset_user_password(self, id: str):
        """
        重置用户密码
        @param id:用户id
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.reset_user_password(id=id)
        data = endpoint(op)
        try:
            res = (op + data).reset_user_password
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_user(self, variables: dict):
        """
        更新用户信息
        @param variables: 更新用户请求数据
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_user_permissions(self, args=None, **kwargs):
        """
        获取已添加规则
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        permissions = op.permissions(
            filter=eval(f"{kwargs}")
        )
        if args:
            permissions.__fields__(*args)
        data = endpoint(op)
        res = (op + data).permissions
        return res

    def get_all_permissions_of_user(self, args=None, **kwargs):
        """
        获取用户能够获得的所有权限信息
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        direct_authorization_rules_of_user = op.all_permissions_of_user(
            filter=eval(f"{kwargs['kwargs']['filter']}"),
            user_id=kwargs['kwargs']['userId']
        )
        if args:
            direct_authorization_rules_of_user.__fields__(*args)
        data = endpoint(op)
        res = (op + data).all_permissions_of_user
        return res

    def get_direct_authorization_rules_of_user(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        direct_authorization_rules_of_user = op.direct_authorization_rules_of_user(
            filter=eval(f"{kwargs['kwargs']['filter']}"),
            user_id=kwargs['kwargs']['userId']
        )
        if args:
            direct_authorization_rules_of_user.data.__fields__(*args)
            direct_authorization_rules_of_user.total_count()

        data = endpoint(op)
        res = (op + data).direct_authorization_rules_of_user
        return res

    def set_authorization_rules_to_user_api(self, variables: dict):
        """
        为用户添加权限规则
        @param variables:dict
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.set_authorization_rules_to_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).set_authorization_rules_to_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def remove_authorization_rules_of_user_api(self, ids: list, userId: str):
        """
        删除用户的一条权限规则
        @param ids:[list] rules id
        @param userId:[str] user id
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.remove_authorization_rules_of_user(ids=ids, user_id=userId)
        data = endpoint(op)
        try:
            res = (op + data).remove_authorization_rules_of_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_authorization_rules_of_user_api(self, variables: dict):
        """
        更新用户的一条权限规则
        @param variables:更新用户请求数据
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_authorization_rules_of_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_authorization_rules_of_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_authorization_rule_and_dependencies(self, rule_id):
        """
        获取一条规则的详细数据
        @param rule_id:已添加规则id
        @return: True or False

        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        authorization_rule_and_dependencies = op.authorization_rule_and_dependencies(id=rule_id)
        data = endpoint(op)
        res = (op + data).authorization_rule_and_dependencies
        return res


if __name__ == '__main__':
    a = User()

    # res = a.get_all_permissions_of_user(args=['app'], kwargs={
    #     "filter": {
    #         "types": [
    #             "MENU",
    #             "PAGE"
    #         ]
    #     },
    #     "userId": "8a19c2dc-b8dc-4633-9bdb-39ee8c0c90d6"
    # })
    # res = a.get_direct_authorization_rules_of_user( args=["id"],kwargs={

    #     "filter": {
    #         "permissionTypes": [
    #             "PAGE"
    #         ]
    #     },
    #     "limit": 50,
    #     "offset": 0,
    #     "userId": "3fffa3c1-ca9d-4455-b133-8a2fbb8ecb38"
    # })
    # res = a.get_user_list({
    #     "includeChildrenOrganizations": False,
    #     "includeDisabledUsers": False,
    #     "organizations": [
    #         {
    #             "id": "a1c97533-4149-4a13-bf73-e4a3bf08a25a"
    #         }
    #     ]
    # })
    res=a.get_user("ada2c2ec0-ab6f-475e-a2b5-acd12c1e5222")

    print(res)