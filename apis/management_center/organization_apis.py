from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import Mutation, Query


class Organization(GetTokenHeader):
    def get_organization_list(self, args=None, **kwargs):
        """
        查看组织下的子组织
        @return: 返回子组织，若不需要子组织下的组织，创建过滤数据时get_organization_list_ask(False)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        organization_list = op.organization_list(
            filter=eval(f"{kwargs}")
        )
        if args:
            organization_list.data.__fields__(*args)
        data = endpoint(op)
        res = (op + data).organization_list
        return res

    def get_organization_tree_nodes(self, args=None):
        """
        获取本公司的所有组织节点
        @param args:过滤结果需要的数据，如：id,name,totalUserCount
        @return:所有的组织节点及其信息
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        organization_tree_nodes = op.organization_tree_nodes()
        if args:
            organization_tree_nodes.__fields__(*args)
        data = endpoint(op)
        res = (op + data).organization_tree_nodes
        return res

    def create_organization_api(self, variables:dict):
        """
        创建组织
        @param variables:[dict]
        @return: true or false
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_organization(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_organization
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_Organization_api(self, variables:dict):
        """
        更新组织
        @param variables: [dict]
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_Organization(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_Organization
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_organization_api(self, org_id:str):
        """
        删除组织
        @param org_id: 组织id
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_organization(id=org_id)
        data = endpoint(op)
        try:
            res = (op + data).delete_organization
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    a = Organization().get_organization_list(kwargs={
        "id": "a1c97533-4149-4a13-bf73-e4a3bf08a25a",
        "isChildrenIncluded": True
    })
    b = Organization().get_organization_tree_nodes(["id"])
    print(b)
