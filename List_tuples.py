import sys

def ec2_names():

    ec2_instances = [f"{sys.argv[1]}", f"{sys.argv[2]}", f"{sys.argv[3]}"]
    print (ec2_instances)
    print (len(ec2_instances))
    print (type(ec2_instances))

    ec2_instances.append(f"{sys.argv[4]}")
    print (ec2_instances)
    print (len(ec2_instances))
    print (type(ec2_instances))
    print (ec2_instances[2])
    new_list = (ec2_instances[0:2])
    print (new_list)

    ec2_instances.remove(f"{sys.argv[3]}")
    print (ec2_instances)
    print (len(ec2_instances))
    print (type(ec2_instances))

    s3_buckets = ("alpha", "beta", "gamma", "delta")
    print (s3_buckets)
    print (len(s3_buckets))
    print (type(s3_buckets))

    numeric_list = [1,5,2,3,4,8,6,7,9,10]
    print (numeric_list)
    print (len(numeric_list))
    print (numeric_list.sort())
    print (numeric_list)

    s3_buckets.append("epsilon")  
    # This will raise an AttributeError since tuples are immutable
    print (s3_buckets)

ec2_names()

