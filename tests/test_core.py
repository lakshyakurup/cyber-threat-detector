from core.engine import DetectionEngine
from utils.config import Settings
from utils.parsers import parse_log_line


def test_signature_rules_cover_common_web_attacks():
    engine = DetectionEngine()
    for payload, name in [
        ("union select password from users", "sql_injection"),
        ("<script>alert(1)</script>", "xss"),
        ("../../etc/passwd", "path_traversal"),
        ("; cat /etc/passwd", "command_injection"),
    ]:
        result = engine.analyze(payload)
        assert result.threat
        assert name in {signature.name for signature in result.signatures}


def test_reputation_and_rate_limit_raise_risk():
    engine = DetectionEngine(Settings(rate_limit=1, reputation_blocklist=frozenset({"10.0.0.1"})))
    assert engine.analyze("normal", source_ip="10.0.0.1").threat
    assert engine.analyze("normal", source_ip="10.0.0.2").threat is False
    assert engine.analyze("normal", source_ip="10.0.0.2").threat


def test_parser_supports_json_and_plain_text():
    assert parse_log_line('{"message": "ok", "source_ip": "127.0.0.1"}')['source_ip'] == "127.0.0.1"
    assert parse_log_line("plain event")["message"] == "plain event"