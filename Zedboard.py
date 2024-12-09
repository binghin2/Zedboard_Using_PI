#include <iostream>
#include <vector>
#include "vart/runner.hpp"
#include "vart/ai_runner.hpp"
#include "xir/graph.hpp"

int main() {
    // 모델 로드 (xmodel 파일)
    std::string model_path = ""; // xmodel 경로
    auto graph = xir::Graph::deserialize(model_path);
    auto runner = vart::Runner::create_runner(graph, vart::Runner::create_runner_config());

    // 이미지 입력 처리
    // (예시: OpenCV로 이미지 읽기 및 전처리)
    cv::Mat img = cv::imread("");  // 카메라 이미지 입력 예시
    cv::resize(img, img, cv::Size(416, 416));     // YOLOv4-tiny의 입력 크기 416 , 512 중 하나 구현예정

    // 배치 데이터 준비
    std::vector<cv::Mat> batch_data = {img};
    
    // FPGA에서 실행
    auto result = runner->execute(batch_data);

    // 결과 처리 (예시: 사람 수 추정)
    // 결과를 바탕으로 출석 체크 등의 로직을 구현
    std::cout << "result :  " << result << std::endl;

    return 0;
}
