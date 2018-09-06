#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

class FirstSubscriber : public rclcpp::Node
{
public:
    FirstSubscriber()
        : Node("first_sub_node")
    {
        mSubscription = this->create_subscription<std_msgs::msg::String>(
            "topic", std::bind(&FirstSubscriber::topic_callback, this, _1));
    }

private:
    void topic_callback(const std_msgs::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str())
    }
    
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr mSubscription;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<FirstSubscriber>());
    rclcpp::shutdown();
    return 0;
}
