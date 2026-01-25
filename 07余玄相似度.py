import numpy as np

# 计算两个向量的点积,2个向量同纬度数字乘积之和
def get_dot(cec_a,vec_b):
    if len(cec_a) != len(vec_b):
        return ValueError("两个向量 必须维度数量相同")
    
    dot_sum = 0
    for a,b in zip(cec_a, vec_b):
        dot_sum+=a*b

    return dot_sum

# 计算两个向量的模长,对向量的每个数字求平方再求和开根号
def get_norm(vec):
    sum_square=0
    for v in vec:
        sum_square+=v*v

    return np.sqrt(sum_square)

# 余玄相似度，2个向量的点积，除以2个向量模长的乘积
def cosine_similarity(vec_a, vec_b):
    dot_sum = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)

    return dot_sum / (norm_a * norm_b)

if __name__ == "__main__":
    vec_a = [0.5,0.5]
    vec_b = [0.7,0.7]
    vec_c = [0.7,0.5]
    vec_d = [-0.6,-0.5]
    print(cosine_similarity(vec_a, vec_b))
    print(cosine_similarity(vec_a, vec_c))
    print(cosine_similarity(vec_a, vec_d))